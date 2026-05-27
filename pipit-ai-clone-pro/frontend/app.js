const audio = document.getElementById("audio")
const preview = document.getElementById("preview")

audio.onchange = () => {
  preview.src = URL.createObjectURL(audio.files[0])
}

async function generateVideo() {

  const photo = document.getElementById("photo").files[0]
  const audioFile = document.getElementById("audio").files[0]
  const prompt = document.getElementById("prompt").value

  document.getElementById("loading").classList.remove("hidden")

  const form = new FormData()
  form.append("photo", photo)
  form.append("audio", audioFile)
  form.append("prompt", prompt)

  const res = await fetch("http://localhost:8000/generate", {
    method: "POST",
    body: form
  })

  const blob = await res.blob()
  const url = URL.createObjectURL(blob)

  document.getElementById("video").src = url
  document.getElementById("download").href = url

  document.getElementById("loading").classList.add("hidden")
}
