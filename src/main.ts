const ORDER = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`|~ \n";

function fromICFP(str: string): string {
	let buf = "";
	for (let i = 0; i < str.length; ++i) {
		const ord = str.charCodeAt(i);
		buf += ORDER[ord - 33];
	}
	return buf;
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
	const response = await fetch('https://boundvariable.space/communicate', {
		headers: {
			'Authorization': 'Bearer 88befdee-f76d-427d-a63f-12238452ce65'
		},
		method: 'POST',
		body: icfpStr,
	});
	const body = await response.text();
	return body;
}

document.addEventListener('DOMContentLoaded', () => {
	document.getElementById("to_human")?.addEventListener('click', () => {
		const text = (document.getElementById('icfp_text') as HTMLTextAreaElement).value;
		(document.getElementById('human_text') as HTMLTextAreaElement).value = fromICFP(text);
	});

	document.getElementById("to_icfp")?.addEventListener('click', () => {
		const text = (document.getElementById('human_text') as HTMLTextAreaElement).value;
		(document.getElementById('icfp_text') as HTMLTextAreaElement).value = toICFP(text);
	});

	document.getElementById("communicate")?.addEventListener('click', async () => {
		const text = (document.getElementById('icfp_text') as HTMLTextAreaElement).value;
		const response = await communicate(text);
		(document.getElementById('icfp_text') as HTMLTextAreaElement).value = response;
	});
});
