// DOMが読み込まれた後に実行されるように設定
document.addEventListener("DOMContentLoaded", function () {
 // ハンバーガーメニューボタン（画像）を取得
 const menuButton = document.querySelector(".hamburger-menu");
 // モバイルメニューを取得
 const mobileMenu = document.getElementById("mobileMenu");
 // 閉じるボタンを取得
 const closeButton = document.getElementById("closeMenuButton");

 // メニューボタンがクリックされた時の処理
 menuButton.addEventListener("click", function () {
  mobileMenu.classList.toggle("hidden");
 });

 // 閉じるボタンがクリックされた時の処理
 closeButton.addEventListener("click", function () {
  mobileMenu.classList.add("hidden");
 });

 //  モバイルメニューの背景部分がクリックされた時の処理を実装したかったがZindexの関係かうまくいかなかった。
 //  mobileMenuBackground.addEventListener("click", function () {
 //   mobileMenu.classList.add("hidden");
 //  });
});

// Ajax を使って views.py の get_total_days 関数を呼び出す
$.ajax({
 url: '{% url "get_total_days" %}',
 type: "GET",
 dataType: "json",
 success: function (response) {
  // 成功時、id="totalDays" の要素に累計日数を設定
  document.getElementById("totalDays").textContent = response.total_days;
 },
 error: function (xhr, status, error) {
  console.error("Error: " + error);
 }
});
