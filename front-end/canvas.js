window.addEventListener("load", () => {
  const canvas = document.querySelector("#canvas");
  const ctx = canvas.getContext("2d");
  const clearbtn = document.querySelector("#clearButton");

  canvas.height = 450;
  canvas.width = 450;

  let painting = false;

  function startPosition() {
    painting = true;
    // draw(e);
  }
  function finishedPosition() {
    painting = false;
    ctx.beginPath();
  }
  ctx.font = "bold 16px sans-serif";
  function draw(e) {
    if (!painting) return;
    ctx.lineWidth = 10;
    ctx.lineCap = "round";

    ctx.lineTo(e.clientX, e.clientY);
    ctx.stroke();
  }
  function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
  }

  canvas.addEventListener("mousedown", startPosition);
  canvas.addEventListener("mouseup", finishedPosition);
  canvas.addEventListener("mouseout", finishedPosition);
  canvas.addEventListener("mousemove", draw);
  clearbtn.addEventListener("click", clearCanvas);
});
