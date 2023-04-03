import { GameCardInterface } from 'features/games'
import { fetchServerSide } from 'lib/fetchServerSide'
import Image from 'next/image'
import Link from 'next/link'

const Checkout = async () => {
  const data = await fetchServerSide<GameCardInterface[]>({
    path: '/games/cart',
  })
  return (
    <>
      <div className="container mx-auto py-16">
        <div className="mx-auto w-full max-w-2xl">
          <div className="overflow-hidden rounded-lg bg-gray-800 shadow-lg">
            <div className="px-6 py-4">
              <div className="mb-2 text-xl font-bold text-white">Your Order:</div>
              <div className="text-white">
                <div>
                  {data?.map(({ title, coverImg, price, link, currency, sale }, id) => (
                    <div className="mx-4 flex justify-between" key={id}>
                      <div className="justify-normal flex">
                        <Link href="/details/id">
                          <Image src={coverImg} width={50} height={50} alt="" />
                        </Link>
                        <h3>
                          <Link href={link}>{title}</Link>
                        </h3>
                      </div>

                      <div>
                        {currency}
                        {sale ? sale : price}
                        {sale && (
                          <s>
                            {currency}
                            {price}
                          </s>
                        )}
                      </div>
                    </div>
                  ))}
                </div>
                <div className="mb-2 flex justify-between">
                  <div>Subtotal:</div>
                  <div>RUB 60.00</div>
                </div>
                <div className="flex justify-between">
                  <div>Total:</div>
                  <div>RUB 60.00</div>
                </div>
              </div>
            </div>
            <div className="px-6 py-4">
              <input
                className="mt-4 w-full appearance-none rounded border-2 border-gray-700 bg-gray-700 py-2 px-4 leading-tight text-white focus:border-gray-500 focus:bg-gray-600 focus:outline-none"
                id="name"
                type="text"
                placeholder="Name"
              />
              <input
                className="mt-4 w-full appearance-none rounded border-2 border-gray-700 bg-gray-700 py-2 px-4 leading-tight text-white focus:border-gray-500 focus:bg-gray-600 focus:outline-none"
                id="email"
                type="text"
                placeholder="Email"
              />
              <input
                className="mt-4 w-full appearance-none rounded border-2 border-gray-700 bg-gray-700 py-2 px-4 leading-tight text-white focus:border-gray-500 focus:bg-gray-600 focus:outline-none"
                id="address"
                type="text"
                placeholder="Address"
              />
              <input
                className="mt-4 w-full appearance-none rounded border-2 border-gray-700 bg-gray-700 py-2 px-4 leading-tight text-white focus:border-gray-500 focus:bg-gray-600 focus:outline-none"
                id="city"
                type="text"
                placeholder="City"
              />
              <input
                className="mt-4 w-full appearance-none rounded border-2 border-gray-700 bg-gray-700 py-2 px-4 leading-tight text-white focus:border-gray-500 focus:bg-gray-600 focus:outline-none"
                id="state"
                type="text"
                placeholder="State"
              />
              <input
                className="mt-4 w-full appearance-none rounded border-2 border-gray-700 bg-gray-700 py-2 px-4 leading-tight text-white focus:border-gray-500 focus:bg-gray-600 focus:outline-none"
                id="zip"
                type="text"
                placeholder="Zip"
              />
            </div>
            <div className="px-6 py-4">
              <Link href="/success">
                <button className="focus:shadow-outline rounded bg-green-500 py-2 px-4 font-bold text-white hover:bg-green-600 focus:outline-none">
                  Place Order
                </button>
              </Link>
            </div>
          </div>
        </div>
      </div>
    </>
  )
}

export default Checkout
