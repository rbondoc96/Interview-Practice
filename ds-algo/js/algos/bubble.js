function bubble(array) {
    let len = array.length

    for(let i = 0; i < len; i++) {
        for(let j = 0; j < len - i - 1; j++) {
            if(array[j] > array[j + 1]) {
                [array[j], array[j + 1]] = [array[j + 1], array[j]]
            }
        }
    }
}

function bubble2(array) {
    let sorted = false

    while(!sorted) {
        sorted = true

        for(let i = 0; i < array.length; i++) {
            if(array[i] > array[i + 1]) {
                [array[i], array[i + 1]] = [array[i + 1], array[i]]
                sorted = false
            }
        }
    }
}


function arraysAreEqual(array1, array2) {
    return (array1.length === array2.length) && (array1.every((elem, idx) => (
        elem === array2[idx]
    )))
}

function test() {
    const array1 = [9, 33, 293, 11, 3, 2]
    const array2 = [9, 33, 293, 11, 3, 2]
    const target = [2, 3, 9, 11, 33, 293]

    console.log(array1)
    console.log(array2)

    let start = performance.now()
    bubble(array1)
    let end = performance.now()
    console.log(`bubble() finished in ${end-start}s.`)

    start = performance.now()
    bubble2(array2)
    end = performance.now()
    console.log(`bubble2() finished in ${end-start}s.`)

    console.log(array1)
    console.log(array2)

    console.log("Did bubble() meet target:", arraysAreEqual(array1, target))
    console.log("Did bubble2() meet target:", arraysAreEqual(array2, target))
}


test()