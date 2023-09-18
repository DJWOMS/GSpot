import { NextResponse } from 'next/server'

const mockData = {
  image: 'https://loremflickr.com/687/376',
  title: 'In CS:GO weakened SG553 and added a new map to the competitive map (H1)',
  date: '11.02.2020, 04:19',
  template: `<p>
        It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of
        using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content
        here', making it look like readable English.
      </p>
      <p>
        Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem
        ipsum' will
        <b>uncover many</b>
        web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour
        and the like).
      </p>
      <h2>Keep Reading (H2)</h2>
      <p>
        There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or
        randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure
        there isn't anything embarrassing hidden in the middle of text.
      </p>
      <h3>Some title(H3)</h3>
      <p>
        All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the
        Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which
        looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.
      </p>
      <p>
        Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it
        over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin
        words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable
        source.
      </p>
      <h4>Some title(H4)</h4>
      <p>
        All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the
        Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which
        looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.
      </p>
      <blockquote>
        If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text.
        All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the
        Internet.
      </blockquote>
      <p>
        It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing
        software like Aldus PageMaker including versions of Lorem Ipsum.
      </p>
      <h5>Some title(H5)</h5>
      <h6>Some title(H6)</h6>
      <p>
        It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks
        reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.
      </p>
      <ul>
        <li>Theme Forest</li>
        <li>Graphic River</li>
        <li>Audio Jungle</li>
        <li>3D Ocean</li>
        <li>Code Canayon</li>
      </ul>
      <p>
        There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or
        randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure
        there isn't anything embarrassing hidden in the middle of text. <a href="#">Link</a>
        the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the
        Internet.
      </p>`,
}

export function GET() {
  return NextResponse.json(mockData)
}
