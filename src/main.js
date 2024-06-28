var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (g && (g = 0, op[0] && (_ = 0)), _) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
var _this = this;
var ORDER = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`|~ \n";
function fromICFP(str) {
    var buf = "";
    for (var i = 0; i < str.length; ++i) {
        var ord = str.charCodeAt(i);
        buf += ORDER[ord - 33];
    }
    return buf;
}
function toICFP(str) {
    var buf = "";
    for (var i = 0; i < str.length; ++i) {
        var ord = ORDER.indexOf(str[i]);
        buf += String.fromCharCode(ord + 33);
    }
    return buf;
}
function communicate(icfpStr) {
    return __awaiter(this, void 0, void 0, function () {
        var response, body;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0: return [4 /*yield*/, fetch('https://boundvariable.space/communicate', {
                        headers: {
                            'Authorization': 'Bearer 88befdee-f76d-427d-a63f-12238452ce65'
                        },
                        method: 'POST',
                        body: icfpStr,
                    })];
                case 1:
                    response = _a.sent();
                    return [4 /*yield*/, response.text()];
                case 2:
                    body = _a.sent();
                    return [2 /*return*/, body];
            }
        });
    });
}
document.addEventListener('DOMContentLoaded', function () {
    var _a;
    var it = document.getElementById('icfp_text');
    var ht = document.getElementById('human_text');
    var cin = document.getElementById('communicate_in');
    var cout = document.getElementById('communicate_out');
    var chuman = document.getElementById('communicate_out_human');
    it.addEventListener('keyup', function (e) {
        ht.value = fromICFP(it.value);
    });
    ht.addEventListener('keyup', function (e) {
        it.value = toICFP(ht.value);
    });
    (_a = document.getElementById("communicate")) === null || _a === void 0 ? void 0 : _a.addEventListener('click', function () { return __awaiter(_this, void 0, void 0, function () {
        var text, response;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    text = cin.value;
                    return [4 /*yield*/, communicate(text)];
                case 1:
                    response = _a.sent();
                    cout.value = response;
                    chuman.value = fromICFP(response);
                    return [2 /*return*/];
            }
        });
    }); });
});
