'use strict'

// teacherPopUp show
function showPopUp(id) {
  const popup = document.getElementById(`teacherPopup-${id}`);
  popup.classList.add("show");
}

// teacherPopUp hide
function hidePopUp(id) {
  const popup = document.getElementById(`teacherPopup-${id}`);
  popup.classList.remove("show");
}

function* uniqueId(prefix = '') {
  let id = 0
  while (true) {
    const _id = id++
    yield `${prefix}-${_id}`
  }
}

const gTeacherId = uniqueId('teacher')

function tempCol(data) {
  const id = gTeacherId.next().value
  const r = `
    <div class="col-12 col-md-4 col-sm-6 teacher-item">
      <div class="popup"${data.imageUrl ? ` onmouseenter="showPopUp('${id}')" onmouseleave="hidePopUp('${id}')` : ''}">
        ${data.imageUrl ? `<img src="${data.imageUrl}" width="100%" alt="${data.name}">` : ''}
        <span class="popuptext${data.imageUrl ? '' : ' show'}" id="teacherPopup-${id}">
          <div class="fill-height overflow-auto scroll-behavior-contain">
            <span class="text-pre-wrap">${data.description}</span>
          </div>
        </span>
      </div>
      <h4>${data.name}</h4>
      <h5>${data.subject}</h5>
    </div>
  `
  return r
}