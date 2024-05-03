document.addEventListener('DOMContentLoaded', function () {
        const svgContainer = document.getElementById('hexagonBox');

        const numRows = 40;
        const numCols = 40;
        const hexWidth = 50;
        const hexHeight = 86.60;

        for (let row = 0; row < numRows; row++) {
            for (let col = 0; col < numCols; col++) {
                const x = col * (hexWidth * 1.5);
                let y = row * hexHeight;
                if (col % 2 === 1) {
                    y += hexHeight / 2;
                }

                const hexagon = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
                hexagon.setAttribute("points", "25 0, 75 0, 100 43.30, 75 86.60, 25 86.60, 0 43.30");
                hexagon.setAttribute("transform", "translate(" + x + "," + y + ")");
                svgContainer.appendChild(hexagon);
            }
        }
    });