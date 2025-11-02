/*!
 * Start Bootstrap - Modern Business v5.0.6 (https://startbootstrap.com/template-overviews/modern-business)
 * Copyright 2013-2022 Start Bootstrap
 * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-modern-business/blob/master/LICENSE)
 */
// This file is intentionally blank
// Use this file to add JavaScript to your project

document.addEventListener("DOMContentLoaded", function () {
  // Quando o modal for aberto
  $("#modal-delete").on("show.bs.modal", function (event) {
    const button = $(event.relatedTarget); // Link que abriu o modal
    const url = button.data("url"); // Pega o data-url do link
    const modalButton = $("#modal-delete-button");

    // Armazena a URL no botão "Deletar"
    modalButton.data("url", url);
  });

  // Quando clicar no botão "Deletar"
  $("#modal-delete-button").on("click", async function () {
    const url = $(this).data("url");

    if (!url) {
      alert("Erro: URL de exclusão não encontrada.");
      return;
    }

    try {
      const response = await fetch(url, { method: "DELETE" });
      if (response.ok) {
        $("#modal-delete").modal("hide");
        window.location.href = "/admin/membro/list";
        //location.reload();
      } else {
        alert("Erro ao excluir o registro.");
      }
    } catch (err) {
      console.error(err);
      alert("Erro de conexão com o servidor.");
    }
  });
});
