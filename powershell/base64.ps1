function b64decode {
    param (
        [string] $b64txt
    );
    $byte = [System.Convert]::FromBase64String($b64txt);
    $txt = [System.Text.Encoding]::Default.GetString($byte);
    return $txt
};

function b64encode {
    param (
        [string] $plaintxt
    );
    $byte = ([System.Text.Encoding]::Default).GetBytes($plaintxt);
    $b64enc = [Convert]::ToBase64String($byte);
    return $b64enc;
};