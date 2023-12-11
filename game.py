import random
import datetime

class Character:
    def __init__(self, name, birth_year, birth_month, birth_day, ushel_year, ushel_month, ushel_day, places, wealth_status, leave_budet):
        self.name = name
        self.birth_year = birth_year
        self.birth_month = birth_month
        self.birth_day = birth_day
        self.age = datetime.datetime.now().year - birth_year
        self.money = leave_budet
        self.ushel_year = ushel_year
        self.ushel_month = ushel_month
        self.ushel_day = ushel_day
        self.places = places
        self.wealth_status = wealth_status
        self.annual_income = 0
        self.player_stocks = [0, 0, 0, 0]

    def get_new_job(self):
        job_options = {
            1: ("TEACHER", 170000, 40000),
            2: ("LAWYER", 800000, 200000),
            3: ("COMPUTER PROGRAMMER", 200000, 50000),
            4: ("BUS DRIVER", 160000, 20000),
            5: ("FOOTBALL PLAYER", 900000, 100000)
        }

        job_number = random.randint(1, 5)

        job_title, base_income, income_variation = job_options[job_number]

        annual_income = base_income + random.randint(0, income_variation) - 10000
        adjusted_income = annual_income - 10000 + random.randint(14000, 26000)

        print(f"YOU GOT A NEW JOB AS A {job_title}. YOU EARN ${annual_income} A YEAR.")
        random_percentage = round(annual_income * random.uniform(0.09, 0.13))
        adjusted_expenses = adjusted_income - random_percentage
        # Увеличиваем self.money на доход от новой работы
        self.money += annual_income
        self.annual_income = annual_income

        print(f"YOU ADJUST YOUR EXPENSES TO ${adjusted_expenses} A YEAR.")
        return adjusted_expenses

    def age_up(self, event_date):
        self.age = event_date.year - self.birth_year
        if self.age >= 65 and random.random() < 0.5:
            print(f"К сожалению, {self.name} умер от старости.")
            return True
        return False

    def earn_money(self, amount):
        self.money += amount

    def coin(self):
        print("YOU ARE OFFERED A COIN SUPPOSEDLY WORTH $100,000.")
        otvet = input("DO YOU BUY IT? (Y/N): ")

        if otvet.upper() == "Y":
            coin_value = random.randint(1, 200000)  # Генерация случайной стоимости монеты от 1 до 200000
            print(f"The coin's value is: ${coin_value}")
            print(f"YOU NOW HAVE {self.money}")
            if coin_value < 100000:
                lost_money = 100000 - coin_value
                self.earn_money(-lost_money)
                return (f"YOU LOST ${lost_money}.")

            else:
                earned_money = coin_value - 100000
                self.earn_money(earned_money)
                return (f"YOU EARNED ${earned_money}.")
        else:
            return "You chose not to buy the coin."
    def JOB(self):
        t = abs(random.randint(10000, 50000))
        print(f"YOU ARE OFFERED ANOTHER JOB FOR $ {t} A YEAR.")
        otvet1 = input("WOULD YOU LIKE TO MOONLIGHT? ")

        if otvet1.upper() == "Y":
            self.earn_money(t)
        else:
            return 0
    def vaction(self):
        otvet1 = input("THE DOCTOR SAYS YOU NEED A VACATION.  DO YOU GO: ")

        if otvet1.upper() == "Y":
            VACATION_value = random.randint(1, 3000)  # Генерация случайной стоимости монеты от 1 до 200000
            print(f"GOOD, THE VACATION COSTS ${VACATION_value}")
            self.earn_money((abs(VACATION_value)) * -1)
            print(f"YOU NOW HAVE {self.money}")
        else:
            return 0
    def granny(self):
        nasl = abs(random.randint(7000, 40000))
        pohorony = abs(random.randint(10000, 42000))
        print("YOUR GRANDFATHER GROVERS JUST DIED. (OH!)  HE LEFT")
        print(f"YOU $ {nasl}, BUT FUNERAL EXPENSES ARE ${pohorony}")
        dohod = nasl - pohorony
        self.earn_money(dohod)

    def gamble(self):
        while True:
            try:
                bet = float(input("YOU GO TO LAS VEGAS TO GAMBLE. HOW MUCH DO YOU BET? "))
                if bet <= 0:
                    return 0

                chance = random.random()  # случайное число от 0 до 1

                if chance > 0.7:
                    loss_amount = -int(random.random() * bet)
                    print(f"HA! HA! YOU LOST ${abs(loss_amount)}")
                    self.earn_money(abs(loss_amount) * -1 )
                    return abs(loss_amount)
                else:
                    win_amount = int((random.random() + random.random()) * bet)
                    print(f"YOU WON ${win_amount}")
                    self.earn_money(abs(win_amount))
                    return abs(win_amount)
            except ValueError:
                print("Please enter a valid number.")


    def boss_say(self):
        frase = ["FIRED", "DECREASE", "RAISE"]
        bos_say = random.choice(frase)
        koff_if_zp = self.annual_income
        if bos_say == "FIRED":
            print(f"YOU'RE FIRED! (HA!)")
            self.earn_money(koff_if_zp * -1)
        elif bos_say == "DECREASE":
            DECREASE = 0.1 * koff_if_zp
            self.earn_money(-1 * DECREASE)
            print(f"YOU GOT A RAISE OF $ {DECREASE} YOU NOW EARN $ {self.money}")

        elif bos_say == "RAISE":
            RAISE = 0.1 * koff_if_zp
            self.earn_money(RAISE)
            print(f"YOU GOT A $ {RAISE} DECREASE IN PAY.  YOU NOW EARN$ {self.money}")

    def ill2(self):
        ill = ["THE ASIO-DISPEPSIA REGIONALY HYPNOTIC FLU!(OH!).", "COMPUTER", "INFECTIOUS FATALY REOCCURING CHRONIC BAD BREATH."]
        illness = random.choice(ill)
        print(f"OH! YOU JUST GOT {illness}")
        if illness == "ASIO-DISPEPSIA":
            self.earn_money(abs(random.randint(3000, 5000)) * -1)
        elif illness == "COMPUTER ITIS.":
            t = abs(random.randint(3000, 5000))
            print(f"HEALTH EXPENSES COST YOU $ {t}")
            self.earn_money( * -1)
        elif illness == "INFECTIOUS FATALY REOCCURING CHRONIC BAD BREATH.":
            t = abs(random.randint(3000, 5000))
            print(f"HEALTH EXPENSES COST YOU $ {t}")


    def ill(self):
        ill = ["A HEART ATTACK", "LEUKEMIA", "CANCER"]
        illness = random.choice(ill)
        print(f"OH! YOU JUST GOT {illness}")
        if illness == "A HEART ATTACK":
            t = abs(random.randint(3000, 5000))
            print(f"MEDICAL BILLS ARE $ {t}")
            self.earn_money(t * -1)
        elif illness == "CANCER":
            t = abs(random.randint(50000, 150000))
            print(f"MEDICAL BILLS ARE $ {t}")
            self.earn_money(t * -1)
        elif illness == "LEUKEMIA":
            t = abs(random.randint(70000, 180000))
            print(f"MEDICAL BILLS ARE $ {t}")
            return "LEUKEMIA"
    def generation(self):
        tamm = [abs(random.randint(1980, 50001)), abs(random.randint(1980, 20001))]
        return random.choice(tamm)

    def FOND_S(self):
        stock_prices = [100, 50, 75, 25]
        while True:
            print("1. IBM (INCREDIBLY BAD MACHINES)")
            print("2. USS (USELESS & STINKY STEEL)")
            print("3. NCR (NO CASH RETURN)")
            print("4. TWA (TOTAL WRECK AIRLINES)")
            choice = input("DO YOU BUY, SELL ($100 FEE), OR NOT (B,S, OR N)")

            if choice.upper() == 'B':
                stock_number = int(input("STOCK : ")) - 1
                quantity = int(input("QUANTITY : "))
                if self.money >= stock_prices[stock_number] * quantity:
                    self.player_stocks[stock_number] += quantity
                    self.earn_money( -1 *  (stock_prices[stock_number] * quantity))
                    print("NOW YOU HAVE", self.player_stocks[stock_number], "акций компании", stock_number + 1)
                else:
                    print("NOT ENOUGH MONEY TO BUY")

            elif choice.upper() == 'S':
                stock_number = int(input("SALES STOCK NUMBER : ")) - 1
                quantity = int(input("QUANTITY : "))
                if self.player_stocks[stock_number] >= quantity:
                    self.player_stocks[stock_number] -= quantity
                    self.earn_money(abs(stock_prices[stock_number] * quantity))
                    print("NOW YOU HAVE", self.player_stocks[stock_number], "STOCK", stock_number + 1)
                else:
                    print("YOU DO NOT HAVE ENOUGH SHARES TO SELL.")

            elif choice.upper() == 'N':
                break



    def FOND_C(self):
        stock_values = sum([self.player_stocks[i] * random.randint(0, 3) for i in range(4)])  # Сумма всех акций игрока
        crash_value = random.randint(0, 3)  # Случайное значение краха рынка

        print("Фондовый рынок рушится! Каждая ваша акция теперь стоит", crash_value)

        money_from_stocks = stock_values * crash_value
        self.earn_money((abs(money_from_stocks)) * -1)   # Деньги, полученные от продажи акций после краха рынка

        print("Вы продали все ваши акции за", money_from_stocks)

    def random_event(self, last_event_date):
        current_year = datetime.datetime.now().year
        last_event_date = datetime.datetime(last_event_date.year, last_event_date.month, last_event_date.day)
        event_date = max(last_event_date, datetime.datetime(2011, 1, 1)) + datetime.timedelta(
            days=random.randint(1, 365 * 10))

        while event_date.year <= 2010:
            event_date = max(last_event_date, datetime.datetime(2011, 1, 1)) + datetime.timedelta(
                days=random.randint(1, 365 * 10))

        events = [
            "YOU JUST HAD A NERVOUS BREAKDOWN.  MEDICAL COSTS!",
            "A TORNADO HAS JUST HIT THE HOME OF ",
            "YOU JUST HAD A CAR ACCIDENT!  MEDICAL COSTS",
            "BOSS say",
            "YOU GO TO LAS VEGAS TO GAMBLE. HOW MUCH DO YOU BET?",
            "YOU ARE OFFERED A COIN SUPPOSEDLY WORTH $100,000.",
            "THE DOCTOR SAYS YOU NEED A VACATION.  DO YOU GO",
            "YOUR HOME HAS BEEN ROBBED OF GOODS WORTH",
            "AN AIRPLANE HAS JUST CRASHED INTO THE HOME OF ",
            "YOUR GRANDFATHER GROVERS JUST DIED. (OH!)  HE LEFT",
            "OH! YOU JUST GOT ",
            "JOB",
            "YOU HAVE ",
            "FOND SELL",
            "FOND CRASH"
        ]


        while True:
            event = random.choice(events)
            if event_date != last_event_date:
                break

        age_at_event = event_date.year - self.birth_year

        print(f"{event_date.strftime('%Y-%m-%d')} ")

        if "GROVERS" in event:
            self.granny()
        elif "BOSS" in event:
            self.boss_say()
        elif "OH! YOU JUST GOT" in event:
            self.ill()
        elif "VEGAS" in event:
            self.gamble()
        elif "COIN" in event:
            self.coin()
        elif "VACATION" in event:
            self.vaction()
        elif "TORNADO" in event:
            t = self.generation()
            print(f"NEWS FLASH!!! "
                  f"A TORNADO HAS JUST HIT THE HOME OF $ {t}")
            self.earn_money(t * -1)
            print(f"YOU NOW HAVE $ {self.money}")
        elif "AIRPLANE" in event:
            t = self.generation()
            print(f"NEWS FLASH!!! "
                  f"AN AIRPLANE HAS JUST CRASHED INTO THE HOME OF $ {t}")
            self.earn_money(t * -1)
            print(f"YOU NOW HAVE $ {self.money}")
        elif "ROBBED" in event:
            t = self.generation()
            print(f"YOUR HOME HAS BEEN ROBBED OF GOODS WORTH $ {t}")
            self.earn_money(t * -1)
            print(f"YOU NOW HAVE $  {self.money}")
        elif "CAR" in event:
            t = abs(random.randint(1000, 3000))
            print(f"YOU JUST HAD A CAR ACCIDENT!  MEDICAL COSTS $ {t}")
            self.earn_money(t * -1)
        elif "NERVOUS" in event:
            t = abs(random.randint(2000, 3000))
            print(f"YOU JUST HAD A NERVOUS BREAKDOWN.  MEDICAL COSTS - $ {t}")
            self.earn_money(t * -1)
        elif "JOB" in event:
            self.JOB()
        elif "FOND SELL " in event:
            self.FOND_S()
        elif "FOND CRASH" in event:
            self.FOND_C()
        elif "YOU HAVE " in event:
            self.ill2()

        if event_date.year != self.birth_year:
            self.age = age_at_event
        return event_date


def generate_random_date():
    birth_year = random.randint(1980, 1990)
    birth_month = random.choice(range(1, 13))  # Выбираем месяц от 1 до 12
    birth_day = random.randint(1, 28)  # Предполагаем, что максимальное количество дней в месяце - 28

    return birth_year, birth_month, birth_day,

def history():
    ushel_year = random.randint(2006, 2010)  # Выбираем год рождения от 1980 до 2005
    ushel_month = random.choice(range(1, 13))  # Выбираем месяц от 1 до 12
    ushel_day = random.randint(1, 28)
    places = ["ON A BIG FARM", "IN A SMALL TOWN"]
    wealth_status = ["YOUR PARENTS ARE VERY RICH.", "YOUR PARENTS ARE VERY POOR."]
    leave_budet = random.randint(400, 10000)
    return ushel_year, ushel_month, ushel_day, random.choice(places), random.choice(wealth_status), leave_budet

def play_game():
    print(f"{'MILLIONAIRE':^40}")
    print(f"{'CREATIVE CQHPUTING':^40}")
    print(f"{'MORRISTOWN, NEW JERSEY':^40}")
    print("\n" * 3)
    name = input("THIS IS THE GAME OF 'MILLIONAIRE'.  ALL YOU MUST DO IS\n"
                 "TYPE IN YOUR NAME AND ANSWER SOME QUESTIONS.  THE\n"
                 "DECISIONS YOU MAKE WILL DETERMINE HOW MUCH MONEY YOU\n"
                 "MAKE.  AT THE TIME OF YOUR DEATH, YOUR LIFE WILL BE\n"
                 "RATED BY THE AMOUNT OF MONEY YOU MADE THROUGHOUT\n"
                 "YOUR LIFE.  IF YOU HAVE MADE $1,000,000 , YOU WILL BE\n"
                 "A MILLIONAIRE AND WIN THE GAME.  NAME PLEASE: ")
    birth_year, birth_month, birth_day = generate_random_date()
    ushel_year, ushel_month,ushel_day, places, wealth_status, leave_budet =history()
    character = Character(name, birth_year, birth_month, birth_day, ushel_year, ushel_month,ushel_day, places, wealth_status, leave_budet)
    month_number_to_name = {
        1: 'JAN',
        2: 'FEB',
        3: 'MAR',
        4: 'APR',
        5: 'MAY',
        6: 'JUN',
        7: 'JUL',
        8: 'AUG',
        9: 'SEP',
        10: 'OCT',
        11: 'NOV',
        12: 'DEC'
    }
    goal_money = 1000000
    last_event_date = datetime.date(character.birth_year, character.birth_month, character.birth_day)
    print(f"New budget after adjusting expenses: $")
    print("\n" * 1)
    print("O.K., ", name,", THIS IS YOUR NEW LIFE!")
    print(places, "ON ",month_number_to_name[birth_month],  " ", birth_day," ,",birth_year,", ", name," IS BORN.")
    print(wealth_status, "ON", month_number_to_name[ushel_month],  " ", ushel_day," ,",ushel_year,", ", "YOU")
    print("LEAVE HOME WITH $", leave_budet)
    adjusted_expenses = character.get_new_job()


    while character.money < goal_money:
        last_event_date = character.random_event(last_event_date)  # Передаем последнюю дату события
        illness_status = character.ill()
        if character.age >= 100: # проверка смерти героя
            break
        elif illness_status == "LEUKEMIA":

            break
        elif illness_status == "HEART ATTACK" and character.age >= 70:
            break


    if character.money >= goal_money:
        print(f"YOU ARE DEAD (COULD'NT TELL, COULD YOU?) AT THE"
              f"AGE OF {character.age}")

        print(f"{character.name} WON!!  YOU ARE A MILLIONAIRE!!"
              f"THANKS FOR PLAYING 'MILLIONAIRE', {character.name}")
    elif character.money > goal_money/2 and goal_money > character.money:
        say = ["NOT BAD", "CLOSE"]
        s1 = random.choice(say)
        if s1 == "NOT BAD":
            print(f"YOU ARE DEAD (COULD'NT TELL, COULD YOU?) AT THE"
                  f"AGE OF {character.age}")
            print(f"NOT BAD, {character.name}"
                  f"THANKS FOR PLAYING 'MILLIONAIRE', {character.name}")
        else:
            print(f"YOU ARE DEAD (COULD'NT TELL, COULD YOU?) AT THE"
                  f"AGE OF {character.age}")
            print(f"CLOSE, {character.name}.  MAYBE NEXT LIFE.")

    else:
        print(f"YOU LOUSY #$%&'*!!! NOW YOUR POOR FAMILY HAS TO PAY."
              f"OFF YOUR DEBTS.......................... "
              f"THANKS FOR PLAYING 'MILLIONAIRE', {character.name}")

if __name__ == "__main__":
    play_game()