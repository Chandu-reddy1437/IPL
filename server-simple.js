import express from 'express';
import cors from 'cors';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());

// Serve team logo images from root directory under /images_final/ path
app.use('/images_final', express.static(__dirname));

// Serve all static files from the project root
app.use(express.static(__dirname));

app.listen(PORT, () => {
    console.log(`🏏 IPL Predictor running at http://localhost:${PORT}`);
});
