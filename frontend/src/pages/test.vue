<template>
    <div id="app" class="container">
      <header>
        <h1>マネーフォワードUS</h1>
        <div class="summary">
          <p>総資産 <span>¥1,000,000</span></p>
          <p>前日比 <span class="increase">+¥30,000</span></p>
        </div>
      </header>
      
      <section class="stats">
        <div class="expenses">
          <h2>支出 ¥52,000</h2>
          <pie-chart :data="expenseData" :labels="expenseLabels" />
        </div>
  
        <div class="income">
          <h2>収入 ¥78,000</h2>
          <pie-chart :data="incomeData" :labels="incomeLabels" />
        </div>
      </section>
  
      <section class="history">
        <ul>
          <li>8月19日（水） 貸し借り -¥1,000</li>
          <li>8月18日（火） 衣服 -¥3,200</li>
          <li>8月15日（土） 収入 +¥10,000</li>
        </ul>
      </section>
  
      <footer>
        <nav>
          <button>HOME</button>
          <button>家計簿</button>
          <button>支出入力</button>
          <button>投稿</button>
        </nav>
      </footer>
    </div>
  </template>
  
  <script>
  import PieChart from './components/PieChart.vue';
  
  export default {
    components: {
      PieChart
    },
    data() {
      return {
        expenseData: [28, 23, 19, 14, 9, 5, 2],
        expenseLabels: ['食費', '趣味・娯楽', '交通費', '変更可能', '変更可能', '変更可能', 'その他'],
        incomeData: [60, 20, 15, 5],
        incomeLabels: ['バイト1', 'バイト2', '変更可能', 'その他']
      };
    }
  };
  </script>
  
  <style scoped>
  .container {
    font-family: Arial, sans-serif;
    padding: 20px;
  }
  header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
  }
  h1 {
    font-size: 24px;
  }
  .summary {
    text-align: right;
  }
  .summary p {
    margin: 0;
  }
  .summary .increase {
    color: blue;
  }
  .stats {
    display: flex;
    justify-content: space-around;
    margin-bottom: 20px;
  }
  .history ul {
    list-style: none;
    padding: 0;
  }
  footer nav {
    display: flex;
    justify-content: space-around;
  }
  button {
    padding: 10px;
  }
  </style>
  