const durations = [2, 3, 5, 2.4, 3, 3.8, 6];
const labels = ["4/10", "4/11", "4/12", "4/13", "4/14", "4/15", "4/16"];

const barChartData = {
 labels: labels,
 datasets: [
  {
   label: "Hours",
   data: durations,
   backgroundColor: "#8AA7A1",
   borderColor: "#8AA7A1",
   borderWidth: 1
  }
 ]
};

const config = {
 type: "bar",
 data: barChartData,
 options: {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
   y: {
    beginAtZero: true,
    ticks: {
     stepSize: 2,
     max: 8
    }
   }
  }
 }
};

const barChart = new Chart(document.getElementById("barChart"), config);
