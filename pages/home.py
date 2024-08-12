from dash import html, register_page  #, callback # If you need callbacks, import it here.
import dash_bootstrap_components as dbc
register_page(
    __name__,
    name='Home',
    top_nav=True,
    path='/'
)


def layout():
    carousel = dbc.Carousel(
        items=[
            {
                "key": "1",
                "src": "/assets/jb.jpg",
                "header": "Auto Valuation Model",
                "caption": "Sistem Pendukung Keputusan di Jawa Barat",
                "img_style": {"width": "100%", "height": "500px"}
            },
            {
                "key": "2",
                "src": "/assets/jb2.jpg",
                "header": "Auto Valuation Model",
                "caption": "Sistem Pendukung Keputusan di Jawa Barat",
                "img_style": {"width": "100%", "height": "500px"}
            },
            {
                "key": "3",
                "src": "/assets/jb3.jpg",
                "header": "Auto Valuation Model",
                "caption": "Sistem Pendukung Keputusan di Jawa Barat",
                "img_style": {"width": "100%", "height": "500px"}
            },
        ],
        controls=True,
        indicators=True,
        interval=3000,
        ride="carousel",
    )

    layout = html.Div(children=[
        dbc.Card(
            dbc.CardBody([
                html.H2("Sistem Pendukung Keputusan Pada Investasi Lahan Tanah Kosong Di Jawa Barat"),
                carousel,
                html.P(
                    "Selamat datang di beranda kami! Temukan informasi terkini tentang lahan kosong di Jawa Barat. "
                    "Dapatkan wawasan tentang kondisi, tren, dan potensi pengembangan lahan ini."
                ),
                html.P(
                    "Dalam upaya untuk memfasilitasi pengambilan keputusan yang lebih cerdas dalam pengelolaan lahan, kami menyajikan analisis "
                    "mendalam yang melibatkan berbagai parameter. Melalui pemahaman "
                    "yang lebih baik terhadap data ini, diharapkan dapat membantu dalam pengembangan lahan tanah "
                    "kosong di Jawa Barat. "
                ),
                html.P(
                    "Sebagai pengguna, Anda dapat dengan mudah melihat status, grafik, dan informasi terkini tentang lahan tanah kosong di Jawa Barat melalui antarmuka yang ramah "
                    "pengguna. Dengan navigasi yang intuitif, Anda dapat menelusuri data berdasarkan kriteria tertentu, melihat prediksi perkembangan lahan, dan memahami perubahan-perubahan "
                    "yang terjadi seiring waktu. Kami berkomitmen untuk menyediakan pengalaman pengguna yang menyeluruh dan memberdayakan, memberikan alat yang diperlukan untuk pengambilan "
                    "keputusan yang lebih cerdas dalam pengelolaan lahan. Selamat menjelajahi dan memanfaatkan sumber daya informasi kami untuk mewujudkan potensi terbaik dari lahan tanah kosong "
                    "di Jawa Barat."
                    "kami juga memberikan fitur clustering dan prediksi. Dengan teknologi"
                    "canggih, kami mengelompokkan lahan-lahan dengan karakteristik serupa ke dalam cluster tertentu, memberikan gambaran yang lebih jelas tentang pola dan tren di "
                    "wilayah ini. Pengguna dapat dengan mudah menjelajahi hasil clustering untuk mendapatkan wawasan yang lebih mendalam tentang potensi dan dinamika lahan tanah kosong "
                    "di Jawa Barat.Selamat mengeksplorasi sumber daya informasi kami"
                ),
                html.P(
                    "Data ini bersumber dari KJPP Rengganis, Hamid dan Rekan. KJPP Rengganis, Hamid & Rekan (KJPP RHR) adalah firma valuation & advisory independen yang menawarkan berbagai layanan "
                    "dalam asset valuation, business valuation, consulting & advisory."
                ),
            ])
        , className="mb-4"),
    ], className="bg-light p-4 m-2")
    return layout
