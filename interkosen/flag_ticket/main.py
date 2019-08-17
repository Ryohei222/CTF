from secret import flag, key
from Crypto.Cipher import AES
from Crypto.Util import Padding
from Crypto import Random
from binascii import hexlify, unhexlify
import json
import responder

api = responder.API()


@api.route("/")
def index(req, resp):
    if "result" in req.cookies:
        api.redirect(resp, api.url_for(result))
    else:
        api.redirect(resp, api.url_for(Check))


@api.route("/exit")
def exit(req, resp):
    resp.set_cookie("user", max_age=-1)
    api.redirect(resp, api.url_for(Check))


@api.route("/result")
def result(req, resp):
    if "result" not in req.cookies:
        api.redirect(resp, api.url_for(Check))
        return

    try:
        cipher = unhexlify(req.cookies["result"])
        if len(cipher) < AES.block_size * 2:
            resp.text = "ERROR: cookie should be iv(16) + cipher(16*n)"
            return
        iv, cipher = cipher[: AES.block_size], cipher[AES.block_size :]
        aes = AES.new(key, AES.MODE_CBC, iv)
        data = Padding.unpad(aes.decrypt(cipher), AES.block_size).decode()
        data = json.loads(data)
        resp.html = api.template("result.html", flag=flag, data=data)
    except TypeError:
        resp.text = "ERROR: invalid cookie"
    except UnicodeDecodeError:
        resp.text = "ERROR: unicode decode error"
    except json.JSONDecodeError:
        resp.text = "ERROR: json decode error"
    except ValueError:
        resp.text = "ERROR: padding error"


@api.route("/check")
class Check:
    def on_get(self, req, resp):
        resp.html = api.template("check.html")

    async def on_post(self, req, resp):
        form = await req.media("form")
        number = form.get("number", None)
        try:
            _ = int(number)
        except ValueError:
            resp.text = "ERROR: please input your ticket number"
            return

        data = json.dumps({"is_hit": False, "number": number}).encode()
        data = Padding.pad(data, AES.block_size)
        iv = Random.get_random_bytes(AES.block_size)
        aes = AES.new(key, AES.MODE_CBC, iv)
        resp.cookies["result"] = hexlify(iv + aes.encrypt(data)).decode()

        api.redirect(resp, api.url_for(result))


if __name__ == "__main__":
    api.run(debug=True)
