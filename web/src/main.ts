import init, { from_icfp } from "./pkg/wasm_interpreter";
const ORDER =
  "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`|~ \n";

async function fromICFP(str: string) {
  try {
    await init();
    return from_icfp(str);
  } catch (error) {
    console.error(error);
    return "";
  }
}

function toICFP(str: string): string {
  let buf = "";
  for (let i = 0; i < str.length; ++i) {
    const ord = ORDER.indexOf(str[i]);
    buf += String.fromCharCode(ord + 33);
  }
  return buf;
}

async function communicate(icfpStr: string): Promise<string> {
  const response = await fetch("https://boundvariable.space/communicate", {
    headers: {
      Authorization: "Bearer 88befdee-f76d-427d-a63f-12238452ce65",
    },
    method: "POST",
    body: icfpStr,
  });
  const body = await response.text();
  return body;
}

document.addEventListener("DOMContentLoaded", () => {
  const it = document.getElementById("icfp_text") as HTMLTextAreaElement;
  const ht = document.getElementById("human_text") as HTMLTextAreaElement;
  const cin = document.getElementById("communicate_in") as HTMLTextAreaElement;
  const cout = document.getElementById(
    "communicate_out"
  ) as HTMLTextAreaElement;
  const chuman = document.getElementById(
    "communicate_out_human"
  ) as HTMLTextAreaElement;

  it.addEventListener("keyup", async () => {
    const value = await fromICFP(it.value);
    ht.value = value;
  });
  ht.addEventListener("keyup", () => {
    it.value = toICFP(ht.value);
  });

  document
    .getElementById("communicate")
    ?.addEventListener("click", async () => {
      const text = cin.value;
      const response = await communicate(text);
      cout.value = response;
      chuman.value = await fromICFP(response);
    });
});
