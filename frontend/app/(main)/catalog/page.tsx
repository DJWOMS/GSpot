import { Breadcrumbs, SectionHead, SectionWrap, SectionTitle, Pagination, Grid, Column20, Column80 } from '@/components'
import { Card, Filter } from '@/features/games'

export default function Page() {
    return (
        <>
            <SectionHead first last>
                <div className="container">
                    <SectionWrap>
                        <SectionTitle>
                            Каталог <span>(35430 игр)</span>
                        </SectionTitle>

                        <Breadcrumbs items={[{ name: 'Каталог' }]} />
                    </SectionWrap>
                </div>
            </SectionHead>

            <section className="section section--last section--catalog">
                <div className="container">
                    <Grid className="row">
                        <Column20 className="col-12">
                            <Filter />
                        </Column20>

                        <Column80 className="col-12">
                            <div className="row">
                                <div className="col-12 col-sm-6 col-md-4 col-xl-3">
                                    <Card title="Hello!" link="#" badge="New" price={30} sale={15} />
                                </div>

                                <div className="col-12 col-sm-6 col-md-4 col-xl-3">
                                    <Card title="We" link="#" price={60} />
                                </div>

                                <div className="col-12 col-sm-6 col-md-4 col-xl-3">
                                    <Card title="Are" link="#" price={70} sale={45} />
                                </div>

                                <div className="col-12 col-sm-6 col-md-4 col-xl-3">
                                    <Card title="React" link="#" price={40} />
                                </div>

                                <div className="col-12 col-sm-6 col-md-4 col-xl-3">
                                    <Card title="Developers!" link="#" price={38} />
                                </div>

                                <Pagination />
                            </div>
                        </Column80>
                    </Grid>
                </div>
            </section>
        </>
    )
}
