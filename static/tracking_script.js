(function() {
    var sendData = function(data) {
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "http://localhost:8080/track", true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send(JSON.stringify(data));
    };

    var trackPageView = function() {
        var data = {
            url: window.location.href,
            referrer: document.referrer,
            timestamp: new Date().toISOString()
        };
        sendData(data);
    };

    window.onload = function() {
        trackPageView();
    };
})();
