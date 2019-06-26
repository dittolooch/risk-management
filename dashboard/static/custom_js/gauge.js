function render_gauge(chart_id, value, name, max_number){
  var chart_div = echarts.getInstanceByDom(
    document.getElementById(chart_id))?echarts.getInstanceByDom(document.getElementById(chart_id)): echarts.init(document.getElementById(chart_id))


  option = {
      tooltip : {
          formatter: "{a} <br/>{b} : {c}"
      },

      series: [
          {
              name: name,
              type: 'gauge',
              min:0,
              max:max_number,
              splitNumber:5,
              detail: {formatter:'{value}'},
              data: [{value: value}]
          }
      ]
  };
  chart_div.setOption(option, notMarge=true)



}
