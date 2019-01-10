using ProgressMeter
using LinearAlgebra
using Plots
gr()
function random_walk(loop)
    one_side = 50
    prob = zeros(Float64,one_side,one_side)
    prob[div(one_side,2),div(one_side,2)]=1.0
    
    progress = Progress(loop)
    anim=@animate for t in 0:loop
        if t == 0
            continue
        else
            next_prob = zeros(Float64,one_side,one_side)
            for x in 1:one_side, y in 1:one_side
                x0 = ((x-1 + (one_side-1)) %one_side) + 1
                x1 = ((x+1 + (one_side-1)) %one_side) + 1
                y0 = ((y-1 + (one_side-1)) %one_side) + 1
                y1 = ((y+1 + (one_side-1)) %one_side) + 1
                next_prob[x,y] = copy( 0.25*prob[x0,y] + 0.25*prob[x1,y] + 0.25*prob[x,y0] + 0.25*prob[x,y1] )
            end
        end
        prob = copy(next_prob)
        next!(progress)
        #println(t,prob)

    heatmap(prob,aspect_ratio=1,cbar=true,cbar_lims=(0,0.025))    
    end
    gif(anim,fps=20)
    
end
random_walk(200)
