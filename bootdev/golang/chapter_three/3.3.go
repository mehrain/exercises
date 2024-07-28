package main

func getMonthlyPrice(tier string) int {
	const dollarToCents = 100
	switch tier {
	case "basic":
		return 100 * dollarToCents
	case "premium":
		return 150 * dollarToCents
	case "enterprise":
		return 500 * dollarToCents
	default:
		return 0
	}
}
