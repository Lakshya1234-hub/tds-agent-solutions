// Let's check all localStorage keys and sessionStorage keys
let ls = {};
for (let i = 0; i < localStorage.length; i++) {
  let k = localStorage.key(i);
  ls[k] = localStorage.getItem(k);
}
return ls;
