import { defineConfig } from "vite";
import { svelte } from "@sveltejs/vite-plugin-svelte";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [svelte()],
  build: {
    outDir: "./dist/www",
    assetsDir: "build",
    rollupOptions: {
      output: {
        entryFileNames: `build/[name].js`,
        chunkFileNames: `build/[name].js`,
        assetFileNames: `build/[name].[ext]`,
      },
    },
  },
});
