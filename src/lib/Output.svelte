<script>
  let prediction = "???";
  let penguin_img = null;

  if (import.meta.env.MODE === "production") {
    Shiny.addCustomMessageHandler("penguin_prediction", (msg) => {
      console.log(msg);
      prediction = msg;
      penguin_img = `penguins/${msg.toLowerCase()}.jpg`;
      console.log(penguin_img);
    });
  }
</script>

<div class="outputs">
  <h2>Predicted penguin...</h2>

  {#if penguin_img !== null}
    <h3>{prediction}!</h3>
    <div class="penguin">
      <img src={penguin_img} alt={prediction} />
    </div>
  {:else}
    <h3>{prediction}</h3>
  {/if}
</div>

<style>
  .outputs {
    width: 64%;
    float: right;
    margin-top: 30px;
  }
  .penguin {
    height: 300px;
    width: auto;
    display: flex;
    object-fit: scale-down;
    margin: 0 auto;
    text-align: center;
  }
</style>
