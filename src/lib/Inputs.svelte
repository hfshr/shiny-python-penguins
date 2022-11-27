<script>
  import { Slider } from "carbon-components-svelte";
  import { RadioButtonGroup, RadioButton } from "carbon-components-svelte";
  import { Button } from "carbon-components-svelte";
  import penguinData from "./penguinData";

  const shinyInput = (id, value) => {
    if (import.meta.env.DEV) {
      console.log(`Sending message to shiny: ${id} = ${JSON.stringify(value)}`);
    } else {
      Shiny.setInputValue(id, value);
    }
  };

  let bill_length = 10;
  let flipper_length = 50;
  let body_mass = 1000;
  let sex = 0;
</script>

<div class="inputs">
  <h2>Inputs</h2>
  <p>Select penguin characteristics and p-p-predict a penguin</p>
  <div class="slider-input">
    <Slider
      bind:value={bill_length}
      min={penguinData.bill_length_mm.min}
      max={penguinData.bill_length_mm.max}
      fullWidth
      labelText="Bill length (mm)"
    />
  </div>
  <div class="slider-input">
    <Slider
      bind:value={flipper_length}
      min={penguinData.flipper_length_mm.min}
      max={penguinData.flipper_length_mm.max}
      fullWidth
      labelText="Flipper length (mm)"
    />
  </div>
  <div class="slider-input">
    <Slider
      bind:value={body_mass}
      fullWidth
      min={penguinData.body_mass_g.min}
      max={penguinData.body_mass_g.max}
      labelText="Body mass (g)"
      step={10}
    />
  </div>
  <div class="radio-input">
    <RadioButtonGroup legendText="Sex" bind:selected={sex}>
      <RadioButton labelText="Female" value={0} />
      <RadioButton labelText="Male" value={1} />
    </RadioButtonGroup>
  </div>

  <div class="btn-container">
    <Button
      size="large"
      class="btn-predict"
      on:click={() =>
        shinyInput(
          "penguin_values",
          JSON.stringify({
            inputs: [bill_length, flipper_length, body_mass, sex],
          })
        )}>P-P-Predict a penguin...!</Button
    >
  </div>
</div>

<style>
  .btn-container {
    margin-top: 10px;
    text-align: center;
  }
  .slider-input {
    margin: 5px;
  }
  .radio-input {
    margin: 5px;
  }
  .inputs {
    padding: 2em;
    margin: 1em;
    border-radius: 10px;
    border: 3px solid #ffffff;
    color: white;
    margin-top: 40px;
    float: left;
    width: 33%;
  }
  div :global(.btn-predict) {
    font-size: large;
    border-radius: 5px;
  }
</style>
