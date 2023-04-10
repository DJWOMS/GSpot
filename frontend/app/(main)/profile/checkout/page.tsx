import Section from 'components/Section'
import { CheckoutGameCard, CheckoutGameCardInterface } from 'features/profile'
import { fetchServerSide } from 'lib/fetchServerSide'
import s from './page.module.scss'

const CheckoutPage = async () => {
  const games = await fetchServerSide<CheckoutGameCardInterface[]>({
    path: '/profile/checkout',
  })

  return (
    <>
      <Section title="Checkout" />

      <Section>
        <div className={s.row}>
          <div className={s.left}>
            <div className={s.checkout}>
              <table className={s.checkoutTable}>
                <colgroup>
                  <col style={{ width: '15%' }} />
                  <col style={{ width: '35%' }} />
                  <col style={{ width: '10%' }} />
                  <col style={{ width: '20%' }} />
                  <col style={{ width: '10%' }} />
                </colgroup>

                <thead>
                  <tr>
                    <th scope="col">Product</th>
                    <th scope="col">Title</th>
                    <th scope="col">Platform</th>
                    <th scope="col">Price</th>
                    <th scope="col"></th>
                  </tr>
                </thead>

                <tbody>{games && games.map((game) => <CheckoutGameCard key={game.id} {...game} />)}</tbody>
              </table>

              <div className={s.checkoutInfo}>
                <div className={s.checkoutTotal}>
                  <p>Total:</p>
                  <span>$27.98</span>
                </div>
              </div>
            </div>
          </div>

          <div className={s.right}>
            <form action="#" className={s.form}>
              <input type="text" className={s.formInput} placeholder="Coupon code" />
              <button type="button" className={s.formBtn}>
                Применить
              </button>
            </form>

            <form action="#" className={s.form}>
              <input type="text" className={s.formInput} placeholder="John Doe" />
              <input type="email" className={s.formInput} placeholder="gg@template.buy" />
              <input type="text" className={s.formInput} placeholder="+1 234 567-89-00" />

              <select name="systems" className={s.formSelect}>
                <option value="visa">Visa</option>
                <option value="mastercard">Mastercard</option>
                <option value="paypal">Paypal</option>
              </select>

              <span className={s.formText}>
                There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form.
              </span>
              <button type="button" className={s.formBtn}>
                Продолжить
              </button>
            </form>
          </div>
        </div>
      </Section>
    </>
  )
}

export default CheckoutPage
