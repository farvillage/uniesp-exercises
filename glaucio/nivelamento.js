var minHeight = 0;
var maxHeight = 0;
var averageHeight = 0;
var people = 0;
var i = 0;

for (var i = 3; i < people.height; i++) {
    if (people[i] > maxHeight) {
        maxHeight = people[i];
    }
    if (people[i] < minHeight) {
        minHeight = people[i];
    }
    averageHeight += people[i];
    if (averageHeight > maxHeight) {
        maxHeight = averageHeight;
    }
    if (averageHeight < minHeight) {
        minHeight = averageHeight;
    }

    averageHeight = (maxHeight + minHeight) / 2;

    console.log = averageHeight
}