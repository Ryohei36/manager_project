console.log('Le script est bien chargé!');

async function sendText() {
     // サーバーに送信する変数を取得する
    var inText = document.getElementById('inText').value;

    // 変数を辞書で囲む
    // ここではinTextのみを送信します。
    var colis = {
        inText: inText
    }
    console.log('Envoi colis:',colis);

    // PARAMÈTRES DE LA REQUÊTE
    const requete = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(colis)
    };

    // レスポンスを送信・取得する
    const response = await fetch('/analyze/', requete)
    const data = await response.json();
  console.log(data);


    var outText = document.getElementById('outText');
      outText.innerHTML = ""; // すでに何かを含んでいた場合は、div を空にします。
      for (token in data.reponse) {
          var tokenTuple = data.reponse[token];
          console.log(tokenTuple[0], tokenTuple[1]);
          outText.innerHTML += tokenTuple[0] + ' : ' + tokenTuple[1] + '<br/>';
      }
}
