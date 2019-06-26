


function render_heatmap(chart_id, chart_data, business_unit, chart_name){

  this_year = new Date().getFullYear()
  last_year = this_year - 1
    var max_count = 0;
    Object.keys(chart_data[business_unit]).forEach(function(yr){
        chart_data[business_unit][yr].forEach(function(d){
            if (d[1]>max_count){
            max_count = d[1]
        }

        })

    })

    var chart_div =echarts.getInstanceByDom(document.getElementById(chart_id))?echarts.getInstanceByDom(document.getElementById(chart_id)): echarts.init(document.getElementById(chart_id))

    var option = {

        animation:true,
        tooltip: {
            position: 'top',
            formatter: function (p) {
                var format = echarts.format.formatTime('yyyy-MM-dd', p.data[0]);
                return format + ': ' + p.data[1];
            }
        },
        visualMap: {
            min: 0,
            max: max_count,
            calculable: true,
            orient: 'horizontal',
            left: 'left',
            top: 'top',
            inRange:{
                color:["#fffffe", bu_color[business_unit]],
            },
        },
        calendar: [
        {
            splitLine:{
                show:true,
                lineStyle:{
                    color:"#c8c9c9",
                     width:4
                }
            },
            range: this_year,
            cellSize: ['auto', 20],
            itemStyle:{
                borderColor:"#c8c9c9"
            }
        },
        {
            splitLine:{
                show:true,
                lineStyle:{
                    color:"#c8c9c9",
                     width:4
                }
            },
            top: 260,
            range: last_year,
            cellSize: ['auto', 20],
            itemStyle:{
                borderColor:"#c8c9c9"
            }
        },
       ],
        series: [{
            type: 'heatmap',
            coordinateSystem: 'calendar',
            calendarIndex: 0,
            data: chart_data[business_unit][this_year]
        }, {
            type: 'heatmap',
            coordinateSystem: 'calendar',
            calendarIndex: 1,
            data: chart_data[business_unit][last_year]
        }, ]

    };
    chart_div.setOption(option,notMerge=true);
    $(`#${chart_id}_title`).text(`Number of ${chart_name} Discovered - ${business_unit}`)
}
function update_heatmap(chart_id, bu){
    render_heatmap(chart_id, heatmap_data[chart_id], bu, heatmap_data[chart_id]["chart_name"])
}
