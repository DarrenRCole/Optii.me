console.log("is this really happening")
var ProfessorSection = React.createClass({
	render: function() {
		return <div id="services" className="services">
			<div className="container">
				<div className="service-box-line">
				</div>
				<div className="service-box">
					<p>SERVICES</p>
				</div>
				<p className="para1">There are many variations of passages of Lorem Ipsum available, 
					but the majority have <span>suffered alteration in some form by 
					injected humour or randomised.</span></p>
				<div className="service-grids">
					<div className="service-grid">
						<div className="fig">
							<span> </span>
						</div>
						<h4>Videography</h4>
						<p>Contrary wipopular belief,Lorem Ipsum is not simply 
						random text It has roots in a piece of
						classical Latin literature from</p>
					</div>
					<div className="service-grid">
						<div className="fig1">
							<span> </span>
						</div>
						<h4>Photography</h4>
						<p>Contrary wipopular belief,Lorem Ipsum is not simply 
						random text It has roots in a piece of
						classical Latin literature from</p>
					</div>
					<div className="service-grid">
						<div className="fig2">
							<span> </span>
						</div>
						<h4>Auditory</h4>
						<p>Contrary wipopular belief,Lorem Ipsum is not simply 
						random text It has roots in a piece of
						classical Latin literature from</p>
					</div>
					<div className="service-grid">
						<div className="fig3">
							<span> </span>
						</div>
						<h4>Marketing</h4>
						<p>Contrary wipopular belief,Lorem Ipsum is not simply 
						random text It has roots in a piece of
						classical Latin literature from</p>
					</div>
					<div className="clearfix"> </div>
				</div>
			</div>
			</div>

	}
});

ReactDOM.render(
	<ProfessorSection />,
	document.getElementById('professor-container')
);