SERVER_URL = "http://127.0.0.1:4000/";
function hexToBase64(str) {
  return btoa(
    String.fromCharCode.apply(
      null,
      str
        .replace(/\r|\n/g, "")
        .replace(/([\da-fA-F]{2}) ?/g, "0x$1 ")
        .replace(/ +$/, "")
        .split(" ")
    )
  );
}

function Notification(Message, SubMessage,kind) {
  E = `<bx-inline-notification
    style="min-width: 30rem; margin-bottom: .5rem"
    title="${Message}"
    subtitle="${SubMessage}"
    hide-close-button	
='true'
kind='${kind}'
  >
  </bx-inline-notification>`;
  const notify = document.createElement("div");
  notify.innerHTML = E;
  notify.style.position = "fixed";
  notify.style.bottom = "10px";
  notify.style.right = "-10000px";

  notify.style.transitionDuration = ".3s";

  setTimeout(() => {
    notify.style.right = "10px";
  }, 1);


  setTimeout(() => {
    notify.style.opacity = 0;

    notify.style.right = "-10000px";
    document.body.removeChild(notify);
  }, 4000);

  document.body.append(notify);
}
