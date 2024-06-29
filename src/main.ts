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

interface Program {
	tokens: string[];
	cur: number;
}

function evaluate(program: Program) {
	const token = program.tokens[program.cur];
}

function execICFP(code: string) {
	const tokens = code.split(' ');
	const program: Program = {
		tokens,
		cur: 0,
	};
	evaluate(program);
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
	const it = document.getElementById('icfp_text') as HTMLTextAreaElement;
	const ht = document.getElementById('human_text') as HTMLTextAreaElement;
	const cin = document.getElementById('communicate_in') as HTMLTextAreaElement;
	const cout = document.getElementById('communicate_out') as HTMLTextAreaElement;
	const chuman = document.getElementById('communicate_out_human') as HTMLTextAreaElement;

	it.addEventListener('keyup', (e) => {
		ht.value = fromICFP(it.value);
	});
	ht.addEventListener('keyup', (e) => {
		it.value = toICFP(ht.value);
	});

	document.getElementById('communicate_echo')?.addEventListener('click', async() => {
		const response = await communicate(`B. S%#(/} ${cin.value}`);
	    cout.value = response;
		chuman.value = fromICFP(response);
	});

	document.getElementById('communicate_command')?.addEventListener('click', async() => {
		const response = await communicate('S' + toICFP(cin.value));
		cout.value = response;
		chuman.value = fromICFP(response);
	});

	document.getElementById("communicate")?.addEventListener('click', async () => {
		const text = cin.value;
		const response = await communicate(text);
		cout.value = response;
		chuman.value = fromICFP(response);
	});
});
