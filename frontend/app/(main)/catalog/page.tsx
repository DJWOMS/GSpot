import Breadcrumbs from 'components/Breadcrumbs'
import Section from 'components/Section'
import Pagination from 'components/Pagination'
import { GameCard, FilterGames } from 'features/games'

export default function Page() {
    return (
        <>
            <Section
                first
                last
                items={[
                    {
                        title: {
                            children: (
                                <>
                                    Каталог <span>(35430 игр)</span>
                                </>
                            ),
                        },
                    },
                ]}
            />
            <Section
                last
                items={[
                    {
                        navigation: [
                            {
                                children: <Breadcrumbs items={[{ name: 'Каталог' }]} />,
                            },
                        ],
                        children: (
                            <section className="section section--last section--catalog">
                                <div className={'flex'}>
                                    <FilterGames />

                                    <div className="w-full">
                                        <div className="grid gap-x-4 grid-cols-4 grid-flow-row">
                                            <div className="w-full">
                                                <GameCard title="Hello!" link="#" badge="New" price={30} sale={15} />
                                            </div>

                                            <div className="w-full">
                                                <GameCard title="We" link="#" price={60} />
                                            </div>

                                            <div className="w-full">
                                                <GameCard title="Are" link="#" price={70} sale={45} />
                                            </div>

                                            <div className="w-full">
                                                <GameCard title="React" link="#" price={40} />
                                            </div>

                                            <div className="w-full">
                                                <GameCard title="Developers!" link="#" price={38} />
                                            </div>
                                        </div>

                                        <Pagination />
                                    </div>
                                </div>
                            </section>
                        ),
                    },
                ]}
            />
        </>
    )
}
