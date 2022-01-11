"use strict";
const overlay = document.querySelector(".overlay");
const socialModal = document.querySelector(".social-modal");
const settingModal = document.querySelector(".settings-modal");
const bullhornIcon = document.querySelector(".bullhorn-icon");
const barsIcon = document.querySelector(".bars-icon");
const btnClose = document.querySelector(".btn-close");
const tablebars = document.querySelectorAll(".tablebar");

const closeSettingsModal = function () {
  settingModal.classList.add("hidden");
  overlay.classList.add("hidden");

  if (settingModal.classList.contains("slide-in-2")) {
    settingModal.classList.remove("slide-in-2");
    settingModal.classList.add("slide-in-1");
  } else {
    settingModal.classList.remove("slide-in-1");
    settingModal.classList.add("slide-in-2");
  }
};

for (let tablebar of tablebars) {
  //https://dev.to/mohdhussein/how-to-show-the-clicked-element-only-and-hide-others-in-vanilla-javascript-1ip2
  tablebar.addEventListener("click", (e) => {
    const current = e.target;
    const active = document.querySelector(".active");

    active.classList.remove("active");
    active.firstElementChild.nextElementSibling.classList.add(
      "tablebar-hide-para"
    );

    current.parentElement.classList.add("active");
    current.nextElementSibling.classList.remove("tablebar-hide-para");
  });
}

bullhornIcon.addEventListener("click", function () {
  socialModal.classList.toggle("hidden");
});

barsIcon.addEventListener("click", function () {
  if (
    !settingModal.classList.contains("slide-in-1") &&
    !settingModal.classList.contains("slide-in-2")
  ) {
    settingModal.classList.add("slide-in-1");
  }

  settingModal.classList.remove("hidden");
  overlay.classList.remove("hidden");
});

overlay.addEventListener("click", closeSettingsModal);
btnClose.addEventListener("click", closeSettingsModal);
