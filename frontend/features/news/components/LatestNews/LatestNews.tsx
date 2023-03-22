import Section from 'components/Section'
import { NewsItem } from 'features/news'

export function LatestNews() {
    return (
        <Section
            items={[
                {
                    title: 'Latest news',
                    children: (
                        <>
                            <div className={'flex gap-4'}>
                                <div className="w-full">
                                    <NewsItem
                                        title={'New hot race from your favorite computer games studio'}
                                        imageSrc={'https://picsum.photos/1001'}
                                        date={'3 h ago'}
                                        category={'NFS'}
                                        size={'big'}
                                        commentsCount={3}
                                        url={'#'}
                                    />
                                </div>

                                <div className="w-full">
                                    <NewsItem
                                        title={'New hot race from your favorite computer games studio'}
                                        imageSrc={'https://picsum.photos/1002'}
                                        date={'3 h ago'}
                                        category={'CS:GO'}
                                        size={'big'}
                                        commentsCount={10}
                                        url={'#'}
                                    />
                                </div>
                            </div>

                            <div className="flex gap-4">
                                <div className="w-full">
                                    <NewsItem
                                        title={'New hot race from your favorite computer games studio'}
                                        imageSrc={'https://picsum.photos/1003'}
                                        date={'3 h ago'}
                                        category={'Overview'}
                                        size={'normal'}
                                        commentsCount={2}
                                        url={'#'}
                                    />
                                </div>

                                <div className="w-full">
                                    <NewsItem
                                        title={'New hot race from your favorite computer games studio'}
                                        imageSrc={'https://picsum.photos/1004'}
                                        date={'3 h ago'}
                                        category={'PC'}
                                        size={'normal'}
                                        commentsCount={0}
                                        url={'#'}
                                    />
                                </div>

                                <div className="w-full">
                                    <NewsItem
                                        title={'New hot race from your favorite computer games studio'}
                                        imageSrc={'https://picsum.photos/1005'}
                                        date={'3 h ago'}
                                        category={'VR'}
                                        size={'normal'}
                                        commentsCount={50}
                                        url={'#'}
                                    />
                                </div>
                            </div>
                        </>
                    ),
                },
            ]}
        />
    )
}
