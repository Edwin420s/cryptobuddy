import random

class CryptoBuddy:
    def __init__(self):
        self.name = "CryptoBuddy"
        self.greetings = [
            "Hey there! Let's find you a green and growing crypto!",
            "Crypto enthusiast detected! How can I help you today?",
            "Welcome to the future of finance! What can I help you with?"
        ]
        
        self.crypto_db = {
            "Bitcoin": {
                "price_trend": "rising",
                "market_cap": "high",
                "energy_use": "high",
                "sustainability_score": 3/10,
                "symbol": "BTC"
            },
            "Ethereum": {
                "price_trend": "stable",
                "market_cap": "high",
                "energy_use": "medium",
                "sustainability_score": 6/10,
                "symbol": "ETH"
            },
            "Cardano": {
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8/10,
                "symbol": "ADA"
            },
            "Solana": {
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 7/10,
                "symbol": "SOL"
            },
            "Algorand": {
                "price_trend": "stable",
                "market_cap": "low",
                "energy_use": "low",
                "sustainability_score": 9/10,
                "symbol": "ALGO"
            }
        }
        
        self.disclaimer = "⚠️ Remember: Crypto is risky—always do your own research! ⚠️"
    
    def greet(self):
        return random.choice(self.greetings)
    
    def respond(self, user_query):
        user_query = user_query.lower()
        
        if any(word in user_query for word in ["hi", "hello", "hey", "greetings"]):
            return self.greet()
            
        elif "sustainable" in user_query or "eco" in user_query or "green" in user_query:
            recommend = max(self.crypto_db, key=lambda x: self.crypto_db[x]["sustainability_score"])
            score = self.crypto_db[recommend]["sustainability_score"]
            return f"Invest in {recommend} ({self.crypto_db[recommend]['symbol']})! 🌱 It's eco-friendly with a sustainability score of {score*10}/10!"
            
        elif "trend" in user_query or "rising" in user_query or "grow" in user_query:
            rising_coins = [coin for coin in self.crypto_db if self.crypto_db[coin]["price_trend"] == "rising"]
            if not rising_coins:
                return "Hmm, nothing seems to be trending up right now. Maybe check back later?"
            
            # Prioritize high market cap coins that are rising
            high_cap_rising = [coin for coin in rising_coins if self.crypto_db[coin]["market_cap"] == "high"]
            if high_cap_rising:
                recommend = random.choice(high_cap_rising)
                return f"{recommend} ({self.crypto_db[recommend]['symbol']}) is trending up with strong market presence! 📈"
            else:
                recommend = random.choice(rising_coins)
                return f"{recommend} ({self.crypto_db[recommend]['symbol']}) is trending up! 🚀"
                
        elif "profit" in user_query or "gain" in user_query or "earn" in user_query:
            # Recommend coins with rising trend and high market cap
            profitable = [coin for coin in self.crypto_db 
                         if self.crypto_db[coin]["price_trend"] == "rising" 
                         and self.crypto_db[coin]["market_cap"] == "high"]
            
            if profitable:
                recommend = random.choice(profitable)
                return f"For potential profits, consider {recommend} ({self.crypto_db[recommend]['symbol']})! 💰"
            else:
                return "Market seems quiet for high-profit opportunities right now. Maybe look at sustainable options?"
                
        elif "long" in user_query or "term" in user_query or "future" in user_query:
            # Balance between sustainability and growth potential
            long_term = [coin for coin in self.crypto_db 
                        if self.crypto_db[coin]["sustainability_score"] >= 6/10 
                        and self.crypto_db[coin]["price_trend"] == "rising"]
            
            if long_term:
                recommend = max(long_term, key=lambda x: self.crypto_db[x]["sustainability_score"])
                return f"For long-term growth, {recommend} ({self.crypto_db[recommend]['symbol']}) looks promising with good sustainability! 🌍📈"
            else:
                return "The market seems uncertain for long-term picks right now."
                
        elif "list" in user_query or "all" in user_query or "options" in user_query:
            response = "Here are the cryptos I track:\n"
            for coin in self.crypto_db:
                details = self.crypto_db[coin]
                response += f"\n{coin} ({details['symbol']}): Trend: {details['price_trend'].title()}, Market Cap: {details['market_cap'].title()}, Sustainability: {details['sustainability_score']*10}/10"
            return response + "\n\n" + self.disclaimer
            
        elif "help" in user_query:
            return """I can help with:
- Sustainable/green crypto recommendations
- Trending/rising cryptos
- Profit potential analysis
- Long-term investment options
- List all tracked cryptos

Try asking things like:
"What's the most sustainable coin?"
"Which crypto is trending up?"
"What should I buy for long-term growth?"
"""
        else:
            return "I'm not sure I understand. Try asking about sustainable cryptos, trending coins, or investment advice. Type 'help' for options."

def main():
    bot = CryptoBuddy()
    print(f"{bot.name}: {bot.greet()}")
    print(bot.disclaimer)
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print(f"{bot.name}: Happy investing! Remember to DYOR (Do Your Own Research)! 👋")
            break
            
        response = bot.respond(user_input)
        print(f"{bot.name}: {response}")

if __name__ == "__main__":
    main()