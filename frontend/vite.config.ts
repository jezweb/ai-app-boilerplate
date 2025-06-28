import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import vuetify from 'vite-plugin-vuetify';
import path from 'path';

export default defineConfig({
  plugins: [
    vue(),
    vuetify({ autoImport: true }),
  ],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  server: {
    host: '0.0.0.0', // Allow access from other devices on the network
    port: 8080,
    proxy: {
      '/api': {
        target: 'http://backend:8000', // Use service name from docker-compose
        changeOrigin: true,
      },
    },
  },
});
