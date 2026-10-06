import streamlit as st
from datetime import date, timedelta
import random
import string

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="MovieBook",
    page_icon="🎬",
    layout="wide"
)

# ============================================================
# CSS - RED + WHITE THEME
# ============================================================

st.markdown("""
<style>

/* MAIN BACKGROUND */
[data-testid="stAppViewContainer"] {
    background-color: #f5f5f5;
}

[data-testid="stHeader"] {
    background-color: white;
}

/* TOP HEADER */
.top-header {
    background-color: white;
    padding: 18px 25px;
    border-radius: 15px;
    border-bottom: 4px solid #e50914;
    margin-bottom: 15px;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.08);
}

.logo {
    color: #e50914;
    font-size: 32px;
    font-weight: bold;
}

/* MAIN TITLE */
.big-title {
    font-size: 45px;
    font-weight: 800;
    color: #e50914;
}

/* MOVIE CARD */
.movie-card {
    background-color: white;
    padding: 15px;
    border-radius: 15px;
    border: 1px solid #dddddd;
    margin-bottom: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
}

.movie-title {
    font-size: 23px;
    font-weight: bold;
    color: #e50914;
}

/* MOVIE POSTER */
.poster {
    border-radius: 12px;
}

/* SCREEN */
.screen {
    text-align: center;
    padding: 12px;
    margin: 25px 0;
    border-radius: 50%;
    border-top: 7px solid #e50914;
    color: #222222;
    font-weight: bold;
}

/* SEAT INFO */
.seat-info {
    background-color: white;
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #dddddd;
    margin-bottom: 20px;
}

/* BOOKING BOX */
.booking-box {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #dddddd;
}

/* BUTTONS */
.stButton > button {
    border-radius: 8px;
    font-weight: bold;
}

/* PRIMARY BUTTON */
button[kind="primary"] {
    background-color: #e50914 !important;
    color: white !important;
    border: none !important;
}

/* FOOTER */
footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# MOVIES
# ============================================================

movies = [

    {
        "title": "Interstellar",
        "genre": "Sci-Fi / Adventure",
        "rating": 8.7,
        "language": "English",
        "duration": "2h 49m",
        "image": "https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg",
        "description": "A team of astronauts travels through space to find a new home for humanity."
    },

    {
        "title": "Inception",
        "genre": "Sci-Fi / Thriller",
        "rating": 8.8,
        "language": "English",
        "duration": "2h 28m",
        "image": "https://image.tmdb.org/t/p/w500/oYuLEt3zVCKq57qu2F8dT7NIa6f.jpg",
        "description": "A skilled thief enters people's dreams to steal and manipulate ideas."
    },

    {
        "title": "Avengers: Endgame",
        "genre": "Action / Adventure",
        "rating": 8.4,
        "language": "English",
        "duration": "3h 1m",
        "image": "https://image.tmdb.org/t/p/w500/or06FN3Dka5tukK1e9sl16pB3iy.jpg",
        "description": "Superheroes work together to defeat a powerful enemy and save the universe."
    },

    {
        "title": "The Dark Knight",
        "genre": "Action / Crime",
        "rating": 9.0,
        "language": "English",
        "duration": "2h 32m",
        "image": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
        "description": "Batman faces a dangerous criminal who creates chaos throughout Gotham City."
    },

    {
        "title": "3 Idiots",
        "genre": "Comedy / Drama",
        "rating": 8.4,
        "language": "Hindi",
        "duration": "2h 50m",
        "image": "https://image.tmdb.org/t/p/w500/66A9MqXOyVFCssoloscwZz7h0b3.jpg",
        "description": "Three college friends experience friendship, education and the pressures of life."
    },

    {
        "title": "Zindagi Na Milegi Dobara",
        "genre": "Adventure / Comedy",
        "rating": 8.2,
        "language": "Hindi",
        "duration": "2h 35m",
        "image": "https://image.tmdb.org/t/p/w500/9vK9t4Y8zX4J5JQ7K8x5VQ4K0xQ.jpg",
        "description": "Three friends travel together and discover new perspectives about life."
    },

    {
        "title": "The Martian",
        "genre": "Sci-Fi / Adventure",
        "rating": 8.0,
        "language": "English",
        "duration": "2h 24m",
        "image": "https://image.tmdb.org/t/p/w500/5BHuvQ6p9kfc091Z8RiFNhCwL4b.jpg",
        "description": "An astronaut becomes stranded on Mars and must use science to survive."
    },

    {
        "title": "Titanic",
        "genre": "Romance / Drama",
        "rating": 7.9,
        "language": "English",
        "duration": "3h 14m",
        "image": "https://image.tmdb.org/t/p/w500/9xjZS2rlVxm8SFx8kPC3aIGCOYQ.jpg",
        "description": "Two people from different social backgrounds fall in love during a historic voyage."
    }
]


# ============================================================
# THEATRES
# ============================================================

theatres = {

    "Hyderabad": [
        "PVR: Forum Sujana Mall",
        "INOX: GVK One Mall",
        "AMB Cinemas",
        "Cinepolis: Mantra Mall"
    ],

    "Bengaluru": [
        "PVR: Orion Mall",
        "INOX: Garuda Mall",
        "Cinepolis: Shantiniketan"
    ],

    "Mumbai": [
        "PVR: Phoenix Mall",
        "INOX: R City Mall",
        "Cinepolis: Andheri"
    ],

    "Delhi": [
        "PVR: Select Citywalk",
        "INOX: Nehru Place",
        "Cinepolis: Pacific Mall"
    ]
}


# ============================================================
# SHOW TIMES
# ============================================================

show_times = [
    "10:00 AM",
    "01:15 PM",
    "04:30 PM",
    "07:30 PM",
    "10:30 PM"
]


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "🏠 Home"

if "selected_movie" not in st.session_state:
    st.session_state.selected_movie = None

if "selected_seats" not in st.session_state:
    st.session_state.selected_seats = []

if "booking" not in st.session_state:
    st.session_state.booking = None

if "payment" not in st.session_state:
    st.session_state.payment = None


# ============================================================
# FUNCTIONS
# ============================================================

def get_movie(title):

    for movie in movies:

        if movie["title"] == title:
            return movie

    return None


def generate_booking_id():

    letters = string.ascii_uppercase
    numbers = string.digits

    return (
        "".join(random.choices(letters, k=3))
        + "-"
        + "".join(random.choices(numbers, k=6))
    )


# ============================================================
# TOP HEADER
# ============================================================

st.markdown("""
<div class="top-header">
    <div class="logo">
        🎬 MovieBook
    </div>
</div>
""", unsafe_allow_html=True)


# ============================================================
# TOP MENU
# ============================================================

menu1, menu2, menu3, menu4, menu5, menu6 = st.columns(6)


with menu1:

    if st.button(
        "🏠 Home",
        use_container_width=True
    ):

        st.session_state.page = "🏠 Home"
        st.rerun()


with menu2:

    if st.button(
        "🎬 Movies",
        use_container_width=True
    ):

        st.session_state.page = "🎬 Movies"
        st.rerun()


with menu3:

    if st.button(
        "🎟️ Book Tickets",
        use_container_width=True
    ):

        st.session_state.page = "🎟️ Book Tickets"
        st.rerun()


with menu4:

    if st.button(
        "🤖 Recommendations",
        use_container_width=True
    ):

        st.session_state.page = "🤖 Recommendations"
        st.rerun()


with menu5:

    if st.button(
        "💳 Payment",
        use_container_width=True
    ):

        st.session_state.page = "💳 Payment"
        st.rerun()


with menu6:

    if st.button(
        "📋 My Booking",
        use_container_width=True
    ):

        st.session_state.page = "📋 My Booking"
        st.rerun()


# ============================================================
# CITY SELECTION
# ============================================================

st.markdown("---")

city = st.selectbox(
    "📍 Select City",
    list(theatres.keys())
)


# ============================================================
# CURRENT PAGE
# ============================================================

page = st.session_state.page


# ============================================================
# HOME
# ============================================================

if page == "🏠 Home":

    st.markdown(
        '<div class="big-title">🎬 MovieBook</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Book your favourite movies quickly and easily 🍿"
    )

    st.success(
        f"📍 Currently showing movies in {city}"
    )

    st.markdown("## 🔥 Popular Movies")

    cols = st.columns(4)


    for i, movie in enumerate(movies[:4]):

        with cols[i]:

            st.image(
                movie["image"],
                use_container_width=True
            )

            st.markdown(
                f"""
                <div class="movie-card">

                <div class="movie-title">
                🎬 {movie["title"]}
                </div>

                <p>⭐ {movie["rating"]}/10</p>

                <p>🎭 {movie["genre"]}</p>

                <p>🌐 {movie["language"]}</p>

                <p>⏱️ {movie["duration"]}</p>

                </div>
                """,
                unsafe_allow_html=True
            )


            if st.button(
                "🎟️ Book Now",
                key=f"home_{i}",
                use_container_width=True
            ):

                st.session_state.selected_movie = movie

                st.session_state.page = "🎟️ Book Tickets"

                st.rerun()


    st.markdown("---")

    st.markdown("## ⭐ Top Rated Movies")


    top_movies = sorted(
        movies,
        key=lambda x: x["rating"],
        reverse=True
    )


    cols = st.columns(4)


    for i, movie in enumerate(top_movies[:4]):

        with cols[i]:

            st.image(
                movie["image"],
                use_container_width=True
            )

            st.write(
                f"🎬 **{movie['title']}**"
            )

            st.write(
                f"⭐ {movie['rating']}/10"
            )


# ============================================================
# MOVIES
# ============================================================

elif page == "🎬 Movies":

    st.title("🎬 Movies")

    search = st.text_input(
        "🔎 Search movie"
    )


    genres = [
        "All",
        "Action",
        "Adventure",
        "Comedy",
        "Drama",
        "Sci-Fi",
        "Romance"
    ]


    selected_genre = st.selectbox(
        "🎭 Select Genre",
        genres
    )


    for i, movie in enumerate(movies):

        search_match = (
            search.lower()
            in movie["title"].lower()
            if search
            else True
        )


        genre_match = (
            selected_genre == "All"
            or selected_genre.lower()
            in movie["genre"].lower()
        )


        if search_match and genre_match:

            col1, col2 = st.columns([1, 3])


            with col1:

                st.image(
                    movie["image"],
                    use_container_width=True
                )


            with col2:

                st.markdown(
                    f"""
                    <div class="movie-card">

                    <div class="movie-title">
                    🎬 {movie["title"]}
                    </div>

                    <p>
                    ⭐ Rating: {movie["rating"]}/10
                    </p>

                    <p>
                    🎭 Genre: {movie["genre"]}
                    </p>

                    <p>
                    🌐 Language: {movie["language"]}
                    </p>

                    <p>
                    ⏱️ Duration: {movie["duration"]}
                    </p>

                    <p>
                    {movie["description"]}
                    </p>

                    </div>
                    """,
                    unsafe_allow_html=True
                )


                if st.button(
                    "🎟️ Book Tickets",
                    key=f"movie_{i}"
                ):

                    st.session_state.selected_movie = movie

                    st.session_state.page = "🎟️ Book Tickets"

                    st.rerun()


# ============================================================
# BOOK TICKETS
# ============================================================

elif page == "🎟️ Book Tickets":

    st.title("🎟️ Book Movie Tickets")


    # --------------------------------------------------------
    # MOVIE
    # --------------------------------------------------------

    movie_names = [
        movie["title"]
        for movie in movies
    ]


    selected_index = 0


    if st.session_state.selected_movie:

        selected_title = (
            st.session_state.selected_movie["title"]
        )

        if selected_title in movie_names:

            selected_index = movie_names.index(
                selected_title
            )


    selected_movie_name = st.selectbox(
        "🎬 Select Movie",
        movie_names,
        index=selected_index
    )


    movie = get_movie(
        selected_movie_name
    )


    st.session_state.selected_movie = movie


    col1, col2 = st.columns([1, 3])


    with col1:

        st.image(
            movie["image"],
            use_container_width=True
        )


    with col2:

        st.markdown(
            f"""
            ### 🎬 {movie["title"]}

            ⭐ Rating: **{movie["rating"]}/10**

            🎭 Genre: **{movie["genre"]}**

            🌐 Language: **{movie["language"]}**

            ⏱️ Duration: **{movie["duration"]}**

            {movie["description"]}
            """
        )


    st.markdown("---")


    # --------------------------------------------------------
    # DATE
    # --------------------------------------------------------

    selected_date = st.date_input(
        "📅 Select Date",
        min_value=date.today(),
        max_value=date.today() + timedelta(days=7)
    )


    # --------------------------------------------------------
    # THEATRE
    # --------------------------------------------------------

    theatre = st.selectbox(
        "🏢 Select Theatre",
        theatres[city]
    )


    # --------------------------------------------------------
    # SHOW
    # --------------------------------------------------------

    selected_time = st.selectbox(
        "🕐 Select Show Time",
        show_times
    )


    # --------------------------------------------------------
    # SEAT CATEGORY
    # --------------------------------------------------------

    st.markdown("## 💺 Select Seat Category")


    seat_type = st.radio(
        "Choose your seat type",
        [
            "Classic - ₹150",
            "Premium - ₹220",
            "Recliner - ₹350"
        ],
        horizontal=True
    )


    if "Classic" in seat_type:

        price = 150

    elif "Premium" in seat_type:

        price = 220

    else:

        price = 350


    # --------------------------------------------------------
    # SCREEN
    # --------------------------------------------------------

    st.markdown(
        '<div class="screen">🎬 SCREEN</div>',
        unsafe_allow_html=True
    )


    st.markdown("### 💺 Select Your Seats")


    st.markdown(
        """
        <div class="seat-info">

        🟢 Available
        &nbsp;&nbsp;&nbsp;&nbsp;

        🔴 Selected

        </div>
        """,
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # 64 CLASSIC SEATS
    # --------------------------------------------------------

    st.caption(
        "Classic section: 8 rows × 8 seats = 64 seats"
    )


    rows = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H"
    ]


    for row in rows:

        st.write(
            f"**Row {row}**"
        )


        cols = st.columns(8)


        for number in range(1, 9):

            seat = f"{row}{number}"


            with cols[number - 1]:

                if seat in st.session_state.selected_seats:

                    button_text = f"🔴 {number}"

                else:

                    button_text = f"🟢 {number}"


                if st.button(
                    button_text,
                    key=f"seat_{seat}"
                ):

                    if seat in st.session_state.selected_seats:

                        st.session_state.selected_seats.remove(
                            seat
                        )

                    else:

                        if len(
                            st.session_state.selected_seats
                        ) < 8:

                            st.session_state.selected_seats.append(
                                seat
                            )

                        else:

                            st.warning(
                                "Maximum 8 seats allowed."
                            )

                    st.rerun()


    # --------------------------------------------------------
    # SUMMARY
    # --------------------------------------------------------

    st.markdown("---")

    st.markdown("## 🧾 Booking Summary")


    seats = st.session_state.selected_seats


    ticket_amount = (
        len(seats) * price
    )


    convenience_fee = (
        len(seats) * 25
    )


    total = (
        ticket_amount
        + convenience_fee
    )


    col1, col2 = st.columns(2)


    with col1:

        st.write(
            f"🎬 **Movie:** {movie['title']}"
        )

        st.write(
            f"🏢 **Theatre:** {theatre}"
        )

        st.write(
            f"📅 **Date:** {selected_date}"
        )

        st.write(
            f"🕐 **Show:** {selected_time}"
        )


    with col2:

        st.write(
            f"💺 **Seats:** "
            f"{', '.join(seats) if seats else 'None'}"
        )

        st.write(
            f"🎟️ **Number of Tickets:** {len(seats)}"
        )

        st.write(
            f"💰 **Ticket Amount:** ₹{ticket_amount}"
        )

        st.write(
            f"🧾 **Convenience Fee:** ₹{convenience_fee}"
        )

        st.write(
            f"### 💰 Total: ₹{total}"
        )


    # --------------------------------------------------------
    # PROCEED
    # --------------------------------------------------------

    if st.button(
        "💳 Proceed to Payment",
        type="primary",
        use_container_width=True
    ):

        if len(seats) == 0:

            st.error(
                "❌ Please select at least one seat."
            )

        else:

            st.session_state.payment = {

                "movie":
                movie["title"],

                "city":
                city,

                "theatre":
                theatre,

                "date":
                str(selected_date),

                "time":
                selected_time,

                "seats":
                seats.copy(),

                "total":
                total
            }


            st.session_state.page = "💳 Payment"

            st.rerun()


# ============================================================
# PAYMENT
# ============================================================

elif page == "💳 Payment":

    st.title("💳 Payment")


    if st.session_state.payment is None:

        st.warning(
            "Please select your movie and seats first."
        )


    else:

        payment = st.session_state.payment


        st.markdown("## 🧾 Order Summary")


        st.write(
            f"🎬 **Movie:** {payment['movie']}"
        )

        st.write(
            f"🏢 **Theatre:** {payment['theatre']}"
        )

        st.write(
            f"📅 **Date:** {payment['date']}"
        )

        st.write(
            f"🕐 **Show:** {payment['time']}"
        )

        st.write(
            f"💺 **Seats:** "
            f"{', '.join(payment['seats'])}"
        )

        st.write(
            f"## 💰 Total: ₹{payment['total']}"
        )


        st.markdown("---")


        payment_method = st.radio(
            "💳 Choose Payment Method",
            [
                "📱 UPI",
                "💳 Credit / Debit Card",
                "🏦 Net Banking",
                "💵 Cash at Counter"
            ]
        )


        if payment_method == "📱 UPI":

            st.text_input(
                "UPI ID",
                placeholder="example@upi"
            )


        elif payment_method == "💳 Credit / Debit Card":

            st.text_input(
                "Card Number",
                placeholder="XXXX XXXX XXXX XXXX"
            )


            col1, col2 = st.columns(2)


            with col1:

                st.text_input(
                    "Expiry",
                    placeholder="MM/YY"
                )


            with col2:

                st.text_input(
                    "CVV",
                    type="password"
                )


        elif payment_method == "🏦 Net Banking":

            st.selectbox(
                "Select Bank",
                [
                    "SBI",
                    "HDFC Bank",
                    "ICICI Bank",
                    "Axis Bank",
                    "Kotak Mahindra Bank"
                ]
            )


        else:

            st.info(
                "You can pay at the theatre counter."
            )


        st.markdown("---")


        if st.button(
            "✅ Pay & Confirm Booking",
            type="primary",
            use_container_width=True
        ):

            booking_id = generate_booking_id()


            payment["booking_id"] = (
                booking_id
            )


            payment["payment_method"] = (
                payment_method
            )


            st.session_state.booking = (
                payment
            )


            st.session_state.selected_seats = []


            st.session_state.page = (
                "📋 My Booking"
            )


            st.rerun()


# ============================================================
# RECOMMENDATIONS
# ============================================================

elif page == "🤖 Recommendations":

    st.title("🤖 Movie Recommendations")


    st.write(
        "Choose a movie and discover similar movies."
    )


    movie_names = [
        movie["title"]
        for movie in movies
    ]


    selected = st.selectbox(
        "🎬 Select Movie",
        movie_names
    )


    selected_movie = get_movie(
        selected
    )


    selected_words = (
        selected_movie["genre"]
        .lower()
        .replace("/", " ")
        .split()
    )


    results = []


    for movie in movies:

        if movie["title"] == selected:

            continue


        score = 0


        for word in selected_words:

            if word in movie["genre"].lower():

                score += 2


        score += (
            movie["rating"] / 10
        )


        results.append(
            (score, movie)
        )


    results.sort(
        key=lambda x: x[0],
        reverse=True
    )


    st.markdown(
        "## ⭐ Recommended For You"
    )


    rec_cols = st.columns(3)


    for i, (score, movie) in enumerate(
        results[:6]
    ):

        with rec_cols[i % 3]:

            st.image(
                movie["image"],
                use_container_width=True
            )


            st.markdown(
                f"""
                <div class="movie-card">

                <div class="movie-title">
                🎬 {movie["title"]}
                </div>

                <p>
                ⭐ {movie["rating"]}/10
                </p>

                <p>
                🎭 {movie["genre"]}
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# MY BOOKING
# ============================================================

elif page == "📋 My Booking":

    st.title("📋 My Booking")


    booking = st.session_state.booking


    if booking is None:

        st.info(
            "🎟️ You don't have any bookings yet."
        )


        if st.button(
            "🎬 Browse Movies"
        ):

            st.session_state.page = (
                "🎬 Movies"
            )

            st.rerun()


    else:

        st.success(
            "🎉 Booking Confirmed Successfully!"
        )


        st.markdown(
            "## 🎟️ Your Movie Ticket"
        )


        col1, col2 = st.columns(
            [1, 2]
        )


        with col1:

            movie = get_movie(
                booking["movie"]
            )


            if movie:

                st.image(
                    movie["image"],
                    use_container_width=True
                )


        with col2:

            st.write(
                f"### 🎬 {booking['movie']}"
            )

            st.write(
                f"🏙️ **City:** "
                f"{booking['city']}"
            )

            st.write(
                f"🏢 **Theatre:** "
                f"{booking['theatre']}"
            )

            st.write(
                f"📅 **Date:** "
                f"{booking['date']}"
            )

            st.write(
                f"🕐 **Show:** "
                f"{booking['time']}"
            )

            st.write(
                f"💺 **Seats:** "
                f"{', '.join(booking['seats'])}"
            )

            st.write(
                f"💰 **Amount:** "
                f"₹{booking['total']}"
            )

            st.write(
                f"💳 **Payment:** "
                f"{booking['payment_method']}"
            )


        st.markdown("---")


        st.info(
            f"🎟️ Booking ID: "
            f"**{booking['booking_id']}**"
        )


        st.success(
            "🍿 Enjoy your movie!"
        )


        if st.button(
            "❌ Cancel Booking"
        ):

            st.session_state.booking = None

            st.session_state.payment = None

            st.session_state.selected_seats = []

            st.success(
                "Booking cancelled successfully."
            )

            st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "🎬 MovieBook | Book Movies • Choose Seats • Enjoy the Show 🍿"
)