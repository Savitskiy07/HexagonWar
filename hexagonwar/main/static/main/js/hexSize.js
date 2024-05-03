document.addEventListener('DOMContentLoaded', function () {
    const svgContainer = document.getElementById('hexagonBox');
    const numRows = 35;
    const numCols = 26;

    // Получаем размеры шестиугольника
    const width = svgContainer.clientWidth * 0.025;
    const height = width * Math.sqrt(3) / 2; // Приближенная высота для правильного шестиугольника
    const xStep = width * 1.5; // Шаг по оси X между шестиугольниками
    const yStep = height * 0.5; // Шаг по оси Y между шестиугольниками

    function fillHexagon(hexagon) {
    // Заливаем выбранный угольник
    hexagon.setAttribute('fill', 'rgb(0,102,51)'); // Можете изменить цвет по своему усмотрению

    // Сохраняем индекс выбранного угольника в Local Storage
    const hexIndex = Array.from(svgContainer.querySelectorAll('polygon')).indexOf(hexagon);
    localStorage.setItem('selectedHexagonIndex', hexIndex);
    }

    for (let row = 0; row < numRows; row++) {
        for (let col = 0; col < numCols; col++) {
            const x = col * xStep + (row % 2 === 1 ? width * 0.75 : 0);
            const y = row * yStep;

            // Создаем шестиугольник
            const points = [
                `${0.25 * width} 0`,
                `${0.75 * width} 0`,
                `${width} ${0.5 * height}`,
                `${0.75 * width} ${height}`,
                `${0.25 * width} ${height}`,
                `0 ${0.5 * height}`
            ];

            const hexagon = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
            hexagon.setAttribute('points', points.join(','));
            hexagon.setAttribute('width', width); // Установка ширины
            hexagon.setAttribute('height', height); // Установка высоты
            hexagon.setAttribute("transform", `translate(${x},${y})`);
            hexagon.setAttribute("fill", 'white');
            hexagon.setAttribute("stroke", 'black');
            hexagon.setAttribute("stroke-width", '1px');
            // Проверяем, является ли текущая ячейка барьером
            if ((row === 13 && col === 10) || (row === 15 && col === 10) || (row === 14 && col === 10))  {
                hexagon.setAttribute("fill", 'rgb(28,28,28)'); // Устанавливаем черный цвет для барьеров
                hexagon.classList.add('barrier'); // Добавляем класс для барьеров
            }

            hexagon.addEventListener('mouseup', function() {
                if (!this.classList.contains('barrier')) {
                    fillHexagon(this); // Запускаем функцию при клике на угольник, если это не барьер
                }
            });
            svgContainer.appendChild(hexagon);
        }
    }
});

