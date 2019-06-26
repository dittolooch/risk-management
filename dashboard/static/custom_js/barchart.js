function render_bar_chart(chart_id, non_stacked_data, business_unit){
  non_stacked_data = non_stacked_data[business_unit]
  var chart_div;
  if (echarts.getInstanceByDom(document.getElementById(chart_id))){
    chart_div = echarts.getInstanceByDom(document.getElementById(chart_id))
  } else {
    chart_div = echarts.init(document.getElementById(chart_id))
  }
  var y_axis = Array()
  var x_axis = Array()
  non_stacked_data.forEach(function(e){
      y_axis.push(e[0])
    }
  )

  non_stacked_data.forEach(function(e){
      x_axis.push(e[1])
    }
  )

  option = {
    color:[bu_color[business_unit]],
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'shadow'
        }
    },
    legend: {
        data: [business_unit]
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis: {
        type: 'value',

    },
    yAxis: {
        type: 'category',
        data: y_axis
    },
    series: [
        {
            name: business_unit,
            type: 'bar',
            data: x_axis
        },

    ]
  };

  chart_div.setOption(option, notMerge=true);


}
function render_stacked_bar_chart(chart_id, stacked_data){
  var chart_div;
  if (echarts.getInstanceByDom(document.getElementById(chart_id))){
    chart_div = echarts.getInstanceByDom(document.getElementById(chart_id))
  } else {
    chart_div = echarts.init(document.getElementById(chart_id))
  }
  var y_axis = Array()
  var banking_count = Array()
  var wholesale_count = Array()
  var aggregation_count = Array()
  stacked_data.forEach(function(e){
      y_axis.push(e[0])
      banking_count.push(e[1].Banking)
      wholesale_count.push(e[1].Wholesale)
      aggregation_count.push(e[1].Aggregation)
  })
  option = {
      color:[bu_color.Banking,bu_color.Wholesale,bu_color.Aggregation],
      tooltip : {
          trigger: 'axis',
          axisPointer : {
              type : 'shadow'
          }
      },
      legend: {
          data: ['Banking', 'Wholesale', "Aggregation"]
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
              name: 'Banking',
              type: 'bar',
              stack: 'total',
              data: banking_count
          },
          {
              name: 'Wholesale',
              type: 'bar',
              stack: 'total',
              data: wholesale_count
          },
          {
              name: 'Aggregation',
              type: 'bar',
              stack: 'total',
              data: aggregation_count
          },
      ]
  };
  chart_div.setOption(option, notMerge=true);

}
