import Breadcrumbs from 'components/Breadcrumbs'
import Section from 'components/Section'
import Pagination from 'components/Pagination'
import GameCard from 'features/games'
import { Filter } from './Filter'

export default function Page() {
    return (
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
                    navigation: [
                        {
                            children: <Breadcrumbs items={[{ name: 'Каталог' }]} />,
                        },
                    ],
                    children: (
                        <section className="section section--last section--catalog">
                            <div className="container">
                                <div className={'grid grid-cols-2'}>
                                    <Filter />

                                    <div className="row">
                                        <div className="col-12 col-sm-6 col-md-4 col-xl-3">
                                            <GameCard title="Hello!" link="#" badge="New" price={30} sale={15} />
                                        </div>

                                        <div className="col-12 col-sm-6 col-md-4 col-xl-3">
                                            <GameCard title="We" link="#" price={60} />
                                        </div>

                                        <div className="col-12 col-sm-6 col-md-4 col-xl-3">
                                            <GameCard title="Are" link="#" price={70} sale={45} />
                                        </div>

                                        <div className="col-12 col-sm-6 col-md-4 col-xl-3">
                                            <GameCard title="React" link="#" price={40} />
                                        </div>

                                        <div className="col-12 col-sm-6 col-md-4 col-xl-3">
                                            <GameCard title="Developers!" link="#" price={38} />
                                        </div>

                                        <Pagination />
                                    </div>
                                </div>
                            </div>
                        </section>
                    ),
                },
            ]}
        />
    )
}
