chrome.webRequest.onBeforeRequest.addListener(function (details) {
  return { redirectUrl: chrome.extension.getURL("voc.html")};
}, {urls: ['https://www.facebook.com/']}, ['blocking']);