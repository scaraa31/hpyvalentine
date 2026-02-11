from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def valentine():
    return render_template_string("""
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Untuk Kamu, Cintaku ❤️</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&family=Great+Vibes&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            scroll-behavior: smooth;
        }

        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #ff9a9e, #fad0c4);
            color: #fff;
            overflow-x: hidden;
        }

        section {
            min-height: 100vh;
            padding: 80px 10%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
        }

        h1, h2 {
            font-family: 'Great Vibes', cursive;
            font-size: 60px;
            margin-bottom: 20px;
        }

        p {
            font-size: 18px;
            max-width: 800px;
            line-height: 1.8;
            margin-bottom: 20px;
        }

        .card {
            background: rgba(255, 255, 255, 0.15);
            padding: 40px;
            border-radius: 20px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(0,0,0,0.2);
            margin: 30px 0;
            width: 100%;
            max-width: 900px;
        }

        .btn-love {
            padding: 15px 40px;
            background: #ff4b5c;
            border: none;
            border-radius: 30px;
            color: white;
            font-size: 18px;
            cursor: pointer;
            transition: 0.3s;
        }

        .btn-love:hover {
            background: #ff1e3c;
            transform: scale(1.1);
        }

        footer {
            padding: 40px;
            text-align: center;
            font-size: 14px;
            background: rgba(0,0,0,0.2);
        }

        .heart {
            position: fixed;
            top: -10px;
            font-size: 20px;
            animation: fall linear infinite;
            color: #fff;
        }

        @keyframes fall {
            to {
                transform: translateY(110vh);
            }
        }
    </style>
</head>
<body>

<section>
    <h1>Untuk Kamu, Cintaku 💖</h1>
    <div class="card">
        <p>
            Hari Valentine ini bukan hanya sekadar tanggal di kalender. 
            Hari ini adalah pengingat betapa berharganya kamu dalam hidupku.
            Kamu adalah senyum yang selalu ingin aku lihat, 
            pelukan yang selalu ingin aku rasakan, 
            dan nama yang selalu terucap dalam setiap doaku.
        </p>
        <p>
            Terima kasih sudah hadir dalam hidupku, 
            membawa warna di setiap hariku, 
            dan membuat dunia terasa lebih hangat.
        </p>
    </div>
</section>

<section>
    <h2>Alasan Aku Mencintaimu 🌹</h2>
    <div class="card">
        <p>❤️ Karena senyummu bisa mengubah hariku yang paling buruk menjadi indah.</p>
        <p>❤️ Karena kamu selalu mendengarkan ceritaku, bahkan saat aku tidak jelas.</p>
        <p>❤️ Karena kamu membuatku ingin menjadi pria yang lebih baik setiap hari.</p>
        <p>❤️ Karena bersamamu, aku merasa pulang.</p>
        <p>❤️ Karena kamu adalah jawaban dari doa-doa yang tidak pernah aku sadari.</p>
    </div>
</section>

<section>
    <h2>Janji Untukmu 💍</h2>
    <div class="card">
        <p>
            Aku berjanji untuk selalu berusaha memahami kamu.
            Aku berjanji untuk tidak menyerah saat keadaan sulit.
            Aku berjanji untuk tetap menggenggam tanganmu, 
            bahkan ketika dunia terasa berat.
        </p>
        <p>
            Aku mungkin tidak sempurna, 
            tapi cintaku padamu akan selalu tulus dan terus bertumbuh.
        </p>
    </div>
</section>

<section>
    <h2>Masa Depan Kita ✨</h2>
    <div class="card">
        <p>
            Aku membayangkan masa depan di mana kita tertawa bersama, 
            melewati hari-hari dengan saling mendukung, 
            dan membangun mimpi yang kita rancang berdua.
        </p>
        <p>
            Aku ingin setiap Valentine berikutnya tetap bersamamu.
            Bahkan bukan hanya Valentine, 
            tapi setiap hari terasa seperti hari penuh cinta.
        </p>
        <button class="btn-love" onclick="alert('Aku mencintaimu, sekarang dan selamanya ❤️')">
            Klik Jika Kamu Juga Sayang Aku 💕
        </button>
    </div>
</section>

<footer>
    Dibuat dengan penuh cinta ❤️ | Selamanya untukmu
</footer>

<script>
    function createHeart() {
        const heart = document.createElement('div');
        heart.classList.add('heart');
        heart.innerText = '💖';
        heart.style.left = Math.random() * 100 + 'vw';
        heart.style.animationDuration = (Math.random() * 3 + 2) + 's';
        document.body.appendChild(heart);
        setTimeout(() => {
            heart.remove();
        }, 5000);
    }

    setInterval(createHeart, 300);
</script>

</body>
</html>
""")

if __name__ == "__main__":
    app.run(debug=True)
