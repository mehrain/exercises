// ?
async function main() {
    try {
        applyDamage(25, 50)
        const message = await promise
        console.log(`Resolved with ${message}`)
        console.log(message)
    } catch (error) {
        console.error(error)
    }
}

main()

function applyDamage(damage, currentHP) {
    return new Promise((resolve) => {
        const newHP = currentHP - damage
        setTimeout(() => {
            resolve(`The player with ${currentHP} hit points suffers ${damage} points of damage and has ${newHP} hit points remaining.`)
        }, 1000)
    })
}
