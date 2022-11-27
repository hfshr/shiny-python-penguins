<script>
  import Inputs from "./lib/Inputs.svelte";
  import "carbon-components-svelte/css/g90.css";
  import Output from "./lib/Output.svelte";
</script>

<main>
  <h1>Shiny python penguins!</h1>
  <h4 class="info">
    This shiny-python app uses a simple decision tree to predict the species of
    penguin from the palmer penguins dataset. The model uses the penguins
    flipper length, bill length, bodymass and sex. The app uses a custom UI
    written using the svelte framework. Checkout the code <a
      href="https://www.github.com/hfshr">here</a
    >!
  </h4>

  <Inputs />
  <Output />
</main>

<style>
  :global(body) {
    padding: 10px;
  }

  .info {
    width: 60%;
  }
</style>
