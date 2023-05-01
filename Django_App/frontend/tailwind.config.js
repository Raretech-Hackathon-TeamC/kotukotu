/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        blackGreen: "#8AA7A1",
        whiteGreen: "#ADC7C2",
        textBlack: "#474747",
        snow: "#F2F2F2",
        orangerange: "#E6BC87",
        graydaisuki: "#D9D9D9"
      }
    },
    fontFamily: {
      NotoSans: ["Noto Emoji", "sans-serif", "Noto Sans JP", "sans-serif"]
    }
  },
  plugins: []
};
