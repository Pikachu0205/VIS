// let svg = d3.select("body")
//             .append("svg")
//             .attr("width", 500)
//             .attr("height", 500);
//
// svg.append("rect")
//     .attr("x", 10)
//     .attr("y", 10)
//     .attr("height", 100)
//     .attr("width", 100)
//     .style("fill", "red");

d3.select("body")
    .selectAll("p")
    .text("Hello world");

var svg = d3.select("body")
    .append("svg")
    .attr("width", 400)
    .attr("height", 400);

// svg.append("rect")
//     .attr("cx","50px")
//     .attr("cy","50px")
//     .attr("width","50px")
//     .attr("height","50px")
//     .attr("fill","red");

var data = [1535, 1000, 2000, 30000,
            666, 777, 888, 4343];

let xScale = d3.scaleLinear()
    .domain([0, data.length])
    .range([0, 200]);

let yScale =d3.scaleLinear()
    .domain([0, 10000])
    .range([100, 0]);

svg.selectAll("rect")
    .data(data)
    .enter()
    .append("rect")
    .attr("x", function (d, i) {
        return i*10+10;
    })
    .attr("y", 10)
    .attr("height", 20)
    .attr("width", 5)
    .style("fill", "red");

// svg.selectAll("rect")
//     .data(data)
//     .enter()
//     .append("rect")
//     .attr("x", (d,i) => xScale(i))
//     .attr("y", d=>yScale(d)+100)
//     .attr("height", d=>100-yScale(d))
//     .attr("width", 15)
//     .style("fill", "red");
