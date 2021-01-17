function changRange(navi) {
    let f = document.getElementById('form1');
    console.log("I'm here");
    // document.getElementByName("btn-next").disabled = true;
    // f,btn-next.disabled = true;
    f.method = 'post';
    f.action = '/navi';
    f.navi.value = navi;
    f.submit();
}

function changeListRange(navi) {
    let f = document.getElementById('form1');
    // document.getElementByName("btn-next").disabled = true;
    // f,btn-next.disabled = true;
    f.method = 'post';
    f.action = '/navi';
    f.navi.value = navi;
    f.submit();
}
