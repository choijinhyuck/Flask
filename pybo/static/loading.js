function showLoading() {
  // 로딩창을 생성하고 body에 추가
  var overlay = document.createElement("div");
  overlay.className = "overlay";
  var spinner = document.createElement("div");
  spinner.className = "spinner";
  overlay.appendChild(spinner);
  document.body.appendChild(overlay);
}

function hideLoading() {
  // 로딩창을 숨김
  var overlay = document.querySelector(".overlay");
  if (overlay) {
    overlay.parentNode.removeChild(overlay);
  }
}

window.onpageshow = function (event) {
  if (event.persisted) {
    hideLoading();
  }
};
