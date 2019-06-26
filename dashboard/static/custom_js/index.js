function render_loss(data, chart_id){
  option = {
    color:[bu_color.Banking,bu_color.Wholesale,bu_color.Aggregation],
      legend: {
          data: ["Banking",'Wholesale','Aggregation'],
          align: 'left',
          left: 10
      },

      tooltip: {},
      xAxis: {
          inverse:true,
          data: data.Aggregation.date,

          silent: false,
          axisLine: {onZero: true},
          splitLine: {show: false},
          splitArea: {show: false}
      },
      yAxis: {
          inverse: false,
          splitArea: {show: false}
      },
      grid: {
          left: 100
      },

      series: [
        {
            name: 'Banking',
            type: 'bar',
            stack: 'one',

            data: data.Banking.loss
        },,
          {
              name: 'Wholesale',
              type: 'bar',
              stack: 'one',

              data: data.Wholesale.loss
          },
          {
              name: 'Aggregation',
              type: 'bar',
              stack: 'one',

              data: data.Aggregation.loss
          },

      ]
  };
  var chart_div = echarts.getInstanceByDom(
    document.getElementById(chart_id))?echarts.getInstanceByDom(document.getElementById(chart_id)): echarts.init(document.getElementById(chart_id))
  chart_div.setOption(option, notMerge=true)

}
function render_bicd_breakdown(data, chart_id){
  var chart_div = echarts.init(document.getElementById(chart_id));
  var y_axis = Array()
  var complaint_count = Array()
  var incident_count = Array()
  data.forEach(function(e){
      y_axis.push(e[chart_id])
      complaint_count.push(e.complaint_count)
      incident_count.push(e.incident_count)
  })
  option = {
      color:["rgba(0,185,115,0.6)","rgba(0,144,105,0.6)"],
      tooltip : {
          trigger: 'axis',
          axisPointer : {
              type : 'shadow'
          }
      },
      legend: {
          data: ['Breaches & Incidents', 'Complaints & Disputes']
      },
      grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
      },
      xAxis:  {
          type: 'value'
      },
      yAxis: {
          type: 'category',
          data: y_axis
      },
      series: [
          {
              name: 'Breaches & Incidents',
              type: 'bar',
              stack: 'total',
              data: incident_count
          },
          {
              name: 'Complaints & Disputes',
              type: 'bar',
              stack: 'total',
              data: complaint_count
          },
      ]
  };
  chart_div.setOption(option);
}
function render_vertical_graph(data, chart_id){
  console.log(data)
  console.log("render v graph")
  var chart_div = echarts.init(document.getElementById(chart_id));
  var y_axis = data.y
  var x_axis = data.x

  option = {
      color:[bu_color.Banking],
      tooltip : {
          trigger: 'axis',
          axisPointer : {
              type : 'shadow'
          }
      },
      legend: {
          data: ['Residual']
      },
      grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
      },
      xAxis:  {
          type: 'value'
      },
      yAxis: {
          type: 'category',
          data: y_axis
      },
      series: [
          {
              name: 'Residual',
              type: 'bar',
          
              data: x_axis
          },

      ]
  };
  chart_div.setOption(option);
}
