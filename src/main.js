import App from "./App.svelte";

if (import.meta.env.MODE === "production") {
  $(document).on("shiny:sessioninitialized", function (event) {
    new App({
      target: document.getElementById("app"),
    });
  });
} else {
  new App({
    target: document.getElementById("app"),
  });
}

// export default app;
